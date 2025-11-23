'''
You are given an array of integers and a target value K.
Your task is to determine all the two distinct numbers in the array
add up to exactly k, obtain the resultant list.

Return:
resultant list, comprising of the element combination

Example

Input:
input_list: [1, 2, 3, 4, 5, 6]
k: 7

Output:
[(1, 6), (2, 5), (3, 4)]
'''


def target_k_sum(input_list, target_k):
    p_set = set()
    result_list = []

    for idx, p_val in enumerate(input_list):
        inner_list = input_list[:idx] + input_list[idx+1:]
        for i_val in inner_list:
            if p_val + i_val == target_k:
                cur_combo = sorted([p_val, i_val])
                cur_combo_tuple = tuple(cur_combo)

                if cur_combo_tuple not in p_set:
                    result_list.append(cur_combo_tuple)
                    p_set.add(cur_combo_tuple)

    return result_list


input_list = [1, 2, 3, 4, 5, 6]
target_k = 7
print(
    target_k_sum(input_list, target_k)
)
