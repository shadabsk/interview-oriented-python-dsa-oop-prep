'''
Given a list a = [1, 2, 3]
create all unique combination

Output:
[[1], [2], [1, 2], [3], [1, 3], [2, 3], [1, 2, 3]]


bits       included elements        subset
0 0 0       none                    []
0 0 1       idx 0 -> 1              [1]
0 1 0       idx 1 -> 2              [2]
0 1 1       idx 0, 1 -> 1, 2        [1, 2]
1 0 0       idx 2 -> 3              [3]
...
'''
result_list = []

input_list = [1, 2, 3]
n = len(input_list)
for mask in range(1, 1 << n):
    combo = []
    for i in range(n):
        if mask & (1 << i):
            combo.append(input_list[i])

    result_list.append(combo)

print(result_list)
