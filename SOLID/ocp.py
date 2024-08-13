# open closed principle
# open for extension, closed for modification

from enum import Enum

class Color(Enum):
    RED = 1
    GREEN = 2
    BLUE = 3

class Size(Enum):
    SMALL = 1
    MEDIUM = 2
    LARGE = 3


class Product:
    def __init__(self, name, color, size):
        self.name = name
        self.color = color
        self.size = size


# ability to filter by different attributes
class ProductFilter:
    def filter_by_color(self, products, color):
        for p in products:
            if p.color == color: yield p

    def filter_by_size(self, products, size):
        for p in products:
            if p.size == size: yield p

    # what we have done above is violated the open close principle
    # we added a new functionality by modification
    # what should have done is extended the functionality by extension

    # suppose we need to create a Class with filter by 2 criterias, we can have c/s/cs
    # now if we need a Class with filter by 3 criterias, we have c,s,w, cs, sw, cw and csw (7 filters in total)
    # similarly, as we increase the attributes in filter, the class could explode

    # so we do this differently (we'll use some of the enterprise patterns)
# Specification


class Specification:
    "Base Class - Determines whether a particular object determines a particular criteria "
    def is_satisfied(self, item):
        pass

class Filter:

    # specification is on the basis of which you filter
    def filter(self, items, specification):
        pass


class ColorSpecification(Specification):
    "Determines whether a particular object determines a particular criteria "

    def __init__(self, color):
        self.color = color

    def is_satisfied(self, item):
        return item.color == self.color


class SizeSpecification(Specification):
    "Determines whether a particular object determines a particular criteria "

    def __init__(self, size):
        self.size = size

    def is_satisfied(self, item):
        return item.size == self.size


class AndSpecification(Specification):
    def __init__(self, *args):
        self.args = args

    def is_satisfied(self, item):
        return all(map(
            lambda spec: spec.is_satisfied(item), self.args))

# Defining Better Filter
class BetterFilter(Filter):
    def filter(self, items, spec):
        for item in items:
            if spec.is_satisfied(item):
                yield item


if __name__ == "__main__":
    apple = Product('Apple', Color.GREEN, Size.SMALL)
    tree = Product('Tree', Color.GREEN, Size.LARGE)
    house = Product('House', Color.BLUE, Size.LARGE)

    products = [apple, tree, house]

    # Showcasing an example of older implementation of filter
    pf = ProductFilter()
    print('Green Products: \n')
    for p in pf.filter_by_color(products, Color.GREEN):
        print(f' - {p.name} is green.')

    # Showcasing an example of newer implementation of Filter
    print(f'Showing new implementation using Specification and Filter Class')
    bf = BetterFilter()
    for p in bf.filter(products, ColorSpecification(Color.GREEN)):
        print(f' - {p.name} is green.')

    print('Large Products:')
    for p in bf.filter(products, SizeSpecification(Size.LARGE)):
        print(f' - {p.name} is Large')

    # implementing Combination of Logic
    print('Large and Blue Items')
    large_blue = AndSpecification(SizeSpecification(Size.LARGE),
                                  ColorSpecification(Color.BLUE))

    for p in bf.filter(products, large_blue):
        print(f' - {p.name} is Large and Blue')
