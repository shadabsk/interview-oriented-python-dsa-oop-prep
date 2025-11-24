'''
n = 5 --> 120 --> 5 * 4 * 3 * 2 * 1
'''


def get_factorial(n):
    factorial_result = 1
    if n < 0:
        return -1

    if n <= 1:
        return factorial_result
    else:
        for i in range(2, n+1):
            factorial_result *= i

    return factorial_result


print(get_factorial(5))


# Using recursion
def get_factorial_using_recursion(n):
    factorial_result = 1
    if n < 0:
        return -1

    if n <= 1:
        return factorial_result

    '''
    '5 -> 4 => 120'
    '4 -> 3 => 24'
    '3 -> 2 => 6'
    '2 -> 1 => 2'
    '''
    return n * get_factorial(n - 1)


print(get_factorial_using_recursion(5))


# Using generator
from collections import deque


def get_factorial_using_generator(n):
    factorial_result = 1
    if n < 0:
        return -1

    if n <= 1:
        yield factorial_result
    else:
        for i in range(2, n+1):
            factorial_result *= i
            yield factorial_result


dequed_list = deque(get_factorial_using_generator(5), maxlen=1)
print(dequed_list)
result = dequed_list.pop()
print(result)
