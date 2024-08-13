# dependency inversion principle
# high level modules should not depend on low level ones
# they should use abstractions instead

from enum import Enum
class Relationship(Enum):
    PARENT = 0
    CHILD = 1
    SIBLING = 2


class Person:
    def __init__(self, name):
        self.name = name


from abc import abstractmethod


class RelationshipBrowser:

    @abstractmethod
    def find_all_children_of(self, name):
        pass


class Relationships(RelationshipBrowser):
    def __init__(self):
        self.relations = []

    def add_parent_and_child(self, parent, child):
        self.relations.append((parent, Relationship.PARENT, child ))
        self.relations.append((child, Relationship.CHILD, parent))

    # why is the implementation better:
    # tomorrow if the class changes, Research class below will not be affected by it
    def find_all_children_of(self, name):
        for r in self.relations:
            if r[0].name == name and r[1] == Relationship.PARENT:
                yield r[2].name


# high level module
class Research:
    def __init__(self, browser, name):
        for p in browser.find_all_children_of(name):
                print(f'{name} has a child called {p}')
            #
            # if r[0].name == 'John' and r[1] == Relationship.PARENT:
            #     print(f'John has a child called {r[2].name}')

    # 1 POTENTIAL PROBLEM: could be how we are storing relations.
    # we are currently using the internal storage mechanism of a lower level class Relationships
    # if tomorrow, its implementation changes, we may have to alter Research accordingly



if __name__ == '__main__':

    parent = Person('John')
    child1 = Person('Chris')
    child2 = Person('Matt')

    relationships = Relationships()
    relationships.add_parent_and_child(parent, child1)
    relationships.add_parent_and_child(parent, child2)

    Research(relationships, 'John')
