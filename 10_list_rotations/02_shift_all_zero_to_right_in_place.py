'''
You are given a list of integers.
Your task is to shift all zeros to the right end of the list while
preserving the relative order of all non-zero elements.

Constraints
The operation must be performed in place.
You are not allowed to create or use any additional lists or arrays.
Only constant extra variables are permitted (O(1) space).
The final arrangement must maintain the original order of all non-zero values.

Example

Input:
[1, 0, 2, 0, 3, 4, 0]

Output:
[1, 2, 3, 4, 0, 0, 0]
'''


input_list = [1, 0, 2, 0, 3, 4, 0]

for idx, val in enumerate(input_list):
    if val == 0:
        zero_elem = input_list.pop(idx)
        input_list.append(zero_elem)

print(input_list)
