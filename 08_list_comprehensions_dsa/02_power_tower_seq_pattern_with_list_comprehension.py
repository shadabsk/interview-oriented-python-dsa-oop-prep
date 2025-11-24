'''
Create power tower/tetration sequence pattern
[1, 1, 1, 2, 4, 16, 3, 9, 81] with list comprehension
'''


print(
    [
        y
        for i in range(1, 4)
        for y in [
            i,
            i**2,
            (i**2)**2
        ]
    ]
)
