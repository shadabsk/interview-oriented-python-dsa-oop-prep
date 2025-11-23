'''
Given an input [1, 2, 3, 4, 5, 6] with k = 13
find all possible combination, reaching k

Output:
[[2, 5, 6], [3, 4, 6], [1, 2, 4, 6], [1, 3, 4, 5]]
'''

from itertools import combinations

input_list = [1, 2, 3, 4, 5, 6]
n = len(input_list)

target_k = 13

result_list = []

for parent_idx in range(2, n+1):
    for comb in combinations(input_list, parent_idx):
        if sum(comb) == target_k:
            result_list.append(list(comb))

print(result_list)
