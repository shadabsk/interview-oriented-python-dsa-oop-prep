# basic method overriding demo -> single inheritance
class A():
    def some(self):
        return 'A'


class B(A):
    def some(self):
        return 'B'


b = B()
print(b.some())


# Multiple inheritance, Basic MRO demo

class A():
    pass


class B():
    pass


class C():
    pass


class D(B, C):
    pass


print(D.__mro__)


# Multiple inheritance, MRO demo for path D -> B -> C -> A

class A():
    pass


class B(A):
    pass


class C(A):
    pass


class D(B, C):
    pass


print(D.__mro__)


# Multiple inheritance, MRO demo for path E -> D -> C -> B -> A

class A():
    pass


class B(A):
    pass


class C():
    pass


class D(C):
    pass


class E(D, B):
    pass


print(E.__mro__)
