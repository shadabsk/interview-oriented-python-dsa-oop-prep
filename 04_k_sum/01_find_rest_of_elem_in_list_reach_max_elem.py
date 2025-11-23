'''
Given input [1, 2, 3, 6]; create a function that returns True
if sum of all the rest of the element except the maximum element (k)
present in a array, reaches k
'''


def apply_bubble_sort(input_list):
    n = len(input_list)
    for p_idx in range(n):
        for i_idx in range(0, n - p_idx - 1):
            if input_list[i_idx] > input_list[i_idx + 1]:
                input_list[i_idx], input_list[i_idx + 1] = (
                    input_list[i_idx + 1], input_list[i_idx]
                )

    return input_list


def perform_sum(sorted_input_list):
    sum_value = 0
    for input_digit in sorted_input_list:
        sum_value += input_digit
    return sum_value


def check_rest_elem_reaching_max_elem(input_list):
    sorted_list = apply_bubble_sort(input_list)
    max_elem = sorted_list.pop()

    return perform_sum(sorted_list) == max_elem


input_list = [1, 3, 2, 7]
print(
    check_rest_elem_reaching_max_elem(input_list)
)
