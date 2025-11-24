'''
You are given an integer N.
A number is considered prime if:

It is greater than 1, and
It has no positive divisors other than 1 and itself.
Your task is to determine whether N is a prime number.

Return:
True if N is prime

Example 1
Input:
N = 7

Output:
True

Explanation:
7 is divisible only by 1 and 7.

Example 2
Input:
N = 12
Output:
False

Explanation:
12 has divisors 2, 3, 4, and 6.
'''

n = 7


def check_is_prime(n):
    if n <= 1:
        return False

    elif n <= 3:
        return True

    elif n % 2 == 0 or n % 3 == 0:
        return False

    else:
        for i in range(2, n//2):
            if n % i == 0:
                return False

    return True


print(
    check_is_prime(n)
)


# optimized version
# 5,7,11,13,17,19,23,29.....


def check_is_prime_optimized(n):
    if n <= 1:
        return False

    elif n <= 3:
        return True

    elif n % 2 == 0 or n % 3 == 0:
        return False

    i = 5
    while i*i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6

    return True


print(
    check_is_prime_optimized(30)
)
