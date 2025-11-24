# left rotation

'''
arr = [1,2,3,4]
n = 1
output = [2,3,4,1]
-------------
arr = [1,2,3,4]
n = 2
output = [3,4,1,2]
--------------
arr = [1,2,3,4]
n = 6
output = [3,4,1,2]
'''


n = 7

arr = [1, 2, 3, 4]

if n > 4:
    n %= 4

print(
    arr[n:] + arr[:n]
)


# right rotation

'''
arr = [1,2,3,4]
n = 1
output = [4,1,2,3]
-------------
arr = [1,2,3,4]
n = 2
output = [3,4,1,2]
--------------
arr = [1,2,3,4]
n = 7
output = [2,3,4,1]
'''


print(
    arr[-n:] + arr[:-n]
)
