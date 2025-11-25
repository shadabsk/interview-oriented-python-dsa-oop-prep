'''
You are given an array of integers.

The array is considered spirally sorted if:
The elements strictly increase up to a single peak, and
After the peak, the elements strictly decrease.

In other words, the sequence should form a clear mountain shape:
increasing section → one peak → decreasing section.
arr[0] <= arr[n-1] <= arr[1] <= arr[n-2] <= arr[2] <= ...

Your task is to determine whether the given array is spirally sorted.
Return: True if the array satisfies the spirally sorted pattern
False otherwise

Example

Input:
[0, 3, 4, 2]

Explanation:
Increasing: 0 < 3 < 4
Decreasing: 4 > 2
This matches the spiral pattern.

Output:
True
'''


def check_is_spirally_sorted(input_list):
    n = len(input_list)
    left = 1
    right = n - 1
    prev = input_list[0]
    turn = 'right'

    while left <= right:
        if turn == 'right':
            if prev > input_list[right]:
                return False
            prev = input_list[right]
            turn = 'left'
            right -= 1

        elif turn == 'left':
            if prev > input_list[left]:
                return False
            prev = input_list[left]
            turn = 'right'
            left += 1

    return True


input_list = [0, 3, 4, 2]
print(
    check_is_spirally_sorted(
        input_list
    )
)


input_list = [0, 2, 4, 2]
print(
    check_is_spirally_sorted(
        input_list
    )
)


input_list = [0, 2, 1, 2]
print(
    check_is_spirally_sorted(
        input_list
    )
)
