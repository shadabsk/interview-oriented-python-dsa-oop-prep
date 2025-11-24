'''
You are given an integer N.
A number is called an Armstrong number (also known as a Narcissistic number)
if the sum of each of its digits raised to the power of the total
number of digits is equal to the number itself.

Your task is to determine whether N is an Armstrong number
using list comprehension.

Return:

True if N is an Armstrong number
False otherwise

Example:

Input:
153

Explanation:
Digits: 1, 5, 3
Number of digits = 3
Compute:
1³ + 5³ + 3³ = 1 + 125 + 27 = 153
Matches the original number.

Output:
True
'''


def is_armstrong(input_digit):
    input_digit_str = str(input_digit)
    power = len(input_digit_str)

    return sum(
        [
            int(digit)**power for digit in input_digit_str
        ]
    ) == input_digit


print(is_armstrong(159))
