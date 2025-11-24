'''
Given an input [1, 1, 1, 1, 3, 3, 2, 4, 4, 4]

achieve the output as [2, 3, 3, 4, 4, 4, 1, 1, 1, 1]
'''

from collections import Counter

input_list = [1, 1, 1, 1, 3, 3, 2, 4, 4, 4]

input_frequency_dict = Counter(input_list)

sorted_tuple = sorted(input_frequency_dict.items(), key=lambda x: x[1])

print(
    [x[0] for x in sorted_tuple for _ in range(x[1])]
)
