class OperatorOverloadingDemo():
    def __init__(self, value):
        self.value = value

    def __add__(self, other):
        if isinstance(other, OperatorOverloadingDemo):
            return OperatorOverloadingDemo(self.value + other.value)
        return OperatorOverloadingDemo(self.value + other)

    def __sub__(self, other):
        if isinstance(other, OperatorOverloadingDemo):
            return OperatorOverloadingDemo(self.value - other.value)
        return OperatorOverloadingDemo(self.value - other)

    def __mul__(self, other):
        if isinstance(other, OperatorOverloadingDemo):
            return OperatorOverloadingDemo(self.value * other.value)
        return OperatorOverloadingDemo(self.value * other)

    def __truediv__(self, other):
        if isinstance(other, OperatorOverloadingDemo):
            return OperatorOverloadingDemo(self.value // other.value)
        return OperatorOverloadingDemo(self.value // other)

    def __floordiv__(self, other):
        if isinstance(other, OperatorOverloadingDemo):
            return OperatorOverloadingDemo(self.value / other.value)
        return OperatorOverloadingDemo(self.value / other)


a1 = OperatorOverloadingDemo(4)
a2 = OperatorOverloadingDemo(2)

# add
print((a1 + a2).value, 'add')
print((a1 + 4).value, 'add value')


# subtract
print((a1 - a2).value, 'subtract')
print((a1 - 4).value, 'subtract value')


# mul
print((a1 * a2).value, 'mul')
print((a1 * 4).value, 'mul value')


# truediv
print((a1 // a2).value, 'truediv')
print((a1 // 4).value, 'truediv value')


# floordiv
print((a1 / a2).value, 'floordiv')
print((a1 / 4).value, 'floordiv value')
