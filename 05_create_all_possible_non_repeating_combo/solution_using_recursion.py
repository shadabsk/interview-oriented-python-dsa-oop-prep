'''
Given a list a = [1, 2, 3]
create all unique combination

Output:
[[1], [1, 2], [1, 2, 3], [1, 3], [2], [2, 3], [3]]
'''

input_list = [1, 2, 3]
n = len(input_list)
result_list = []


def backtrack(start, path):
    if path:
        result_list.append(path[:])
    for i in range(start, n):
        path.append(input_list[i])
        backtrack(i + 1, path)
        path.pop()


backtrack(0, [])

print(result_list)