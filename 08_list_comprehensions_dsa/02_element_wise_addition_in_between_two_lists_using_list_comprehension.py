'''
Perform element-wise addition between two lists using list comprehension

Example

Input:
list_1 = [1, 2, 3]
list_2 = [4, 5, 6]

Output:
[5, 7, 9]
'''

list_1 = [1, 2, 3]
list_2 = [4, 5, 6]

print(
    [
        x+y
        for x, y in zip(list_1, list_2)
    ]
)
