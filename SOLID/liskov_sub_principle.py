# liskov substitution principle
# you should be able to substitute base type for sub type in a particular functionality and it should work as intended

# if there is an interface, that takes some sort of base class.
# then we should be able to stick a derived class within the interface, and everything should work

# in the below example, we demo the violation of Liskov Substitution Principle
# use_it() function was designed keeping a rectangle in mind but using it on square gives different value
# therefore, implementation is broken

# one way to resolve the problem would have been to simply not create the Square Class.
# but instead create a check attribute within the Rectangle class to see if it is a square or not


class Rectangle:
    def __init__(self, width, height):
        self._width = width
        self._height = height

    @property
    def area(self):
        return self._height * self._width

    def __str__(self):
        return f'Width: {self.width}, Height: {self.height}'

    @property
    def width(self):
        return self._width

    @width.setter
    def width(self, value):
        self._width = value

    @property
    def height(self):
        return self._height

    @height.setter
    def height(self, value):
        self._height = value

    def is_square(self):
        return self.height == self.width


class Square(Rectangle):
    def __init__(self, size):
        Rectangle.__init__(self, size, size)

    # here in below functions, whenever someone sets the height or weight,
    # they end up setting both
    @Rectangle.width.setter
    def width(self, value):
        self._width = self._height = value

    @Rectangle.height.setter
    def height(self, value):
        self._width = self._height = value


def use_it(rc):
    w = rc.width
    rc.height = 10
    expected = int(w*10)
    print(f'Expected an area of {expected}, but got an area of {rc.area}')


if __name__ == '__main__':
    r = Rectangle(2,3)
    use_it(r)

    sq = Square( 5)
    use_it(sq)

    print(f'Is r a square?: {r.is_square()}')