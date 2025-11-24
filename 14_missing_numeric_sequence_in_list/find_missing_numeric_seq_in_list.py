'''
You are given a sorted list of unique positive integers.
Your task is to identify all the integers that are missing between
the minimum and maximum values of the list.

A number is considered missing if it lies within the range
[min(list), max(list)]
but does not appear in the list.

Return the list of all missing numbers in ascending order.

Example

Input:
[1, 2, 3, 6, 7, 9, 10]

Output:
[4, 5, 8]

Explanation:
The full range is 1 to 10.
Numbers 4, 5, and 8 are not present in the input list, so they are
returned as missing numbers.
'''


def find_missing_numeric_sequence(input_list):
    stack = [input_list[0]]
    missing_seq_list = []
    for val in input_list[1:]:
        last_digit = stack[-1]
        if val != last_digit + 1:
            for missing_num in range(last_digit + 1, val):
                missing_seq_list.append(missing_num)
                stack.append(missing_num)

        stack.append(val)

    print(stack)
    return missing_seq_list


input_list = [1, 2, 3, 6, 7, 9, 10]
print(
    find_missing_numeric_sequence(
        input_list
    )
)
