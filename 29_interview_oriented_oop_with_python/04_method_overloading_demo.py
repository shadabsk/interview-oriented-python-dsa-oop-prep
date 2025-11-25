from functools import singledispatchmethod


class MethodOverloadingDemo():
    @singledispatchmethod
    def some(self, args):
        raise NotImplementedError('Unspported Type')

    @some.register
    def _(self, a: int, b: int):
        return 'int operation'

    @some.register
    def _(self, a: str, b: str, c: str):
        return 'str operation'


a = MethodOverloadingDemo()
print(a.some(1, 1))
print(a.some('shadab', 's', 'k'))


# Minimal method overloading demo with *args and **kwargs

class MethodOverloadingMinimalDemoWithDynamicArgument:
    def func(self, *args, **kwargs):
        if args:
            return sum(args)
        if kwargs:
            return sum(kwargs.values())
        return 0


d = MethodOverloadingMinimalDemoWithDynamicArgument()
print(f"d.func(1, 2, 3): {d.func(1, 2, 3)}")
print(f"d.func(a=10, b=20): {d.func(a=10, b=20)}")
print(f"d.func(1, 2, x=5): {d.func(1, 2, x=5)}")
