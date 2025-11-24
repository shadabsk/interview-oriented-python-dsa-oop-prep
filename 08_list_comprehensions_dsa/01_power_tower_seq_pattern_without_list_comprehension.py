'''
Create power tower/tetration sequence pattern
[1, 1, 1, 2, 4, 16, 3, 9, 81]
'''


pattern_list = []
for i in range(1, 4):
    inner_list = [
        i,
        i**2,
        (i**2)**2
    ]
    for inner_elem in inner_list:
        pattern_list.append(inner_elem)


print(pattern_list)
