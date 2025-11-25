'''
Inteface Saggregation Principle (ISP) - Client should not be forced in
implementing methods that they do not want or consume.
'''


from abc import ABC, abstractmethod


class Eater(ABC):
    @abstractmethod
    def eat(self):
        pass


class Flyer(ABC):
    @abstractmethod
    def fly(self):
        pass


class Dog(Eater):
    def eat(self):
        print('Dog eating')


class Parrot(Eater, Flyer):
    def eat(self):
        print('parrot eating')

    def fly(self):
        print('parrot flying')
