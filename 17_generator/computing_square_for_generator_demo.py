'''
Given a list, you are expected to get all the individual element square
using generator

Example:

Input:
[2, 4, 6]

Output:
[4, 8, 36]
'''


def compute_square(input_list):
    for val in input_list:
        yield val ** 2


input_list = [2, 4, 6]
for val in compute_square(input_list):
    print(val)
