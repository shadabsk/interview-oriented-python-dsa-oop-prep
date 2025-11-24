'''
apply bubble sort

Input:
[5, 3, 1, 2, 4]

Output:
[1, 2, 3, 4, 5]
'''


input_list = [5, 3, 1, 2, 4]

'''
p_idx = 0
[3, 5, 1, 2, 4]
[3, 1, 5, 2, 4]
[3, 1, 2, 5, 4]
[3, 1, 2, 4, 5]

[3, 1, 2, 4, 5]
p_idx = 1
[1, 3, 2, 4, 5]
[1, 2, 3, 4, 5]
'''


print('before', input_list)
n = len(input_list)

for parent_idx in range(n):
    for inner_idx in range(0, n - parent_idx - 1):
        if input_list[inner_idx] > input_list[inner_idx + 1]:
            input_list[inner_idx], input_list[inner_idx + 1] = (
                input_list[inner_idx + 1], input_list[inner_idx]
            )
        # just for demo
    if parent_idx == 0:
        print('current_state', input_list)

print('after', input_list)
