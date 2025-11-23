'''
You are given an array of integers and a target value K.
Your task is to determine all the two distinct numbers
and their indices in the array
add up to exactly k, obtain the resultant list.

Return:
resultant list, comprising of the element combination

Example

Input:
input_list: [1, 2, 3, 4, 5, 6]
k: 7

Output:
[(1, 6), (2, 5), (3, 4)]

[(0, 5), (1, 4), (2, 3)]
'''


def target_k_sum(input_list, target_k):
    def find_indices(input_list):
        element_idx_info = {}
        for idx, element in enumerate(input_list):
            element_idx_info[element] = idx

        return element_idx_info

    p_set = set()
    result_list = []
    result_idx_list = []

    element_idx_info = find_indices(input_list)

    for p_val in input_list:
        remainder = abs(p_val - target_k)

        if remainder in element_idx_info:
            cur_combo_tuple = tuple(
                sorted(
                    [
                        p_val,
                        remainder
                    ]
                )
            )
            if cur_combo_tuple not in p_set:
                result_list.append(cur_combo_tuple)
                result_idx_list.append(
                    tuple(
                        sorted(
                            [
                                element_idx_info[p_val],
                                element_idx_info[remainder]

                            ]
                        )
                    )
                )
                p_set.add(cur_combo_tuple)

    return result_list, result_idx_list


input_list = [1, 2, 3, 4, 5, 6]
target_k = 7
result_list, result_idx_list = target_k_sum(input_list, target_k)

print(result_list)
print(result_idx_list)
