'''
You are given a list that may contain integers or other nested lists
at any depth.
Your task is to flatten the list into a single list of integers,
preserving the left-to-right order of elements.

Return the fully flattened list.

Example:

Input:
[[0, 0], 1, [2, [3, 4], 5, [6, 7]]]

Output:
[0, 0, 1, 2, 3, 4, 5, 6, 7]
'''

flattened_list = []


def flatten(sample_input_list):
    for val in sample_input_list:
        if isinstance(val, list):
            flatten(val)
        else:
            flattened_list.append(val)

    return flattened_list


sample_input_list = [[0, 0], 1, [2, [3, 4], 5, [6, 7]]]
print(
    flatten(
        sample_input_list
    )
)
