'''
n = 6 --> [0, 1, 1, 2, 3, 5] --> 0 + 1 + 1 + 2 + 3
'''


def generate_fibonacci_using_generator(n):
    a, b = 0, 1
    for _ in range(n):
        yield a
        a, b = b, a + b


print(list(generate_fibonacci_using_generator(6)))
