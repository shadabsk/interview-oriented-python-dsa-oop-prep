'''
You are given an array of five positive integers.
Your task is to calculate:

Minimum Sum: The smallest possible sum of upto k.
Maximum Sum: The largest possible sum of upto k.

Constraint:
Do not use any internal sorting function

Return the two values.
k = 2

Example

Input:
[3, 1, 2, 4, 5]

Output: -> [max_sum, min_sum]
[12, 3]
'''


def apply_bubble_sort(input_list):
    n = len(input_list)
    for parent_idx in range(n):
        for inner_idx in range(0, n - parent_idx - 1):
            if input_list[inner_idx] > input_list[inner_idx + 1]:
                input_list[inner_idx], input_list[inner_idx + 1] = (
                    input_list[inner_idx + 1], input_list[inner_idx]
                )

    return input_list


def find_max_sum(sorted_input_list, k):
    return sum(sorted_input_list[k:])


def find_min_sum(sorted_input_list, k):
    return sum(sorted_input_list[:k])


def find_max_min_sum(input_list, k):
    sorted_input_list = apply_bubble_sort(input_list)
    return [
        find_max_sum(sorted_input_list, k),
        find_min_sum(sorted_input_list, k)
    ]


input_list = [3, 1, 2, 4, 5]
k = 2

print(
    find_max_min_sum(input_list, k)
)
