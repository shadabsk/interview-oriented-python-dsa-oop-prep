'''
Given an input "bbaaccccfff"

achieve the output as "aabbfffcccc"
'''

from collections import Counter
from operator import itemgetter

input_str = "bbaaccccfff"

input_frequency_dict = Counter(input_str)

sorted_tuple = sorted(input_frequency_dict.items(), key=itemgetter(1))

stack = []
p_set = set()

for idx, cur_tuple in enumerate(sorted_tuple):
    if (
        stack and ord(cur_tuple[0]) < ord(stack[-1][0]) and
        cur_tuple[1] in p_set
    ):
        stack.insert(idx - 1, cur_tuple)
    else:
        stack.append(cur_tuple)
        p_set.add(cur_tuple[1])

print(
    "".join([x[0]*x[1] for x in stack])
)
