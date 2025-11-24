'''
Given two input strings a = 's#h#a#d' b = 'a#bs#k'
whenever you encounter # treat it as backspace.
then finally check if a matches b

Output:
False

Explanation:
post processing of a results to "d"
post processing of b results to "bk"
'''


def hash_as_backspace_process(input_str):
    stack = []
    for char in input_str:
        if char != '#':
            stack.append(char)
        else:
            stack.pop()

    return "".join(stack)


a = "s#h#a#d"
b = "a#bs#k"
print(
    hash_as_backspace_process(a) == hash_as_backspace_process(b)
)

a = "s#h#a#d"
b = "a#b#a#d"
print(
    hash_as_backspace_process(a) == hash_as_backspace_process(b)
)
