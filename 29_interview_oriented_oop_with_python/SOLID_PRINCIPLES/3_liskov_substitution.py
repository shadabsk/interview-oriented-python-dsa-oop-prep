'''
Liskov Substitution Principle (LSP) - Child class should not change/alter
the behaviour of the parent classes.
'''


class Bird:
    pass


class FlyingBird(Bird):
    def fly(self):
        print('Flying')


class Penguin(Bird):
    def swim(self):
        print('Swimming')
