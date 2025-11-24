'''
apply binary search

Example

Input:
input_list = [1, 2, 3, 4, 5]
target = 2

Output:
2, True
'''


def binary_search(input_list, target):
    left = 0
    n = len(input_list)
    right = n - 1
    while (left <= right):
        mid = left + (right - left) // 2

        if input_list[mid] == target:
            return mid, True

        if input_list[mid] > target:
            right = mid - 1
        else:
            left = mid + 1

    return -1, False


print(
    binary_search(
        [1, 2, 3, 4, 5],
        4
    )
)
