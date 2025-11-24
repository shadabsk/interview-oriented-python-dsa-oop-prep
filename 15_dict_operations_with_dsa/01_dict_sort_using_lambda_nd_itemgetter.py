'''
Given a dictionary, describing character count in a word, sort it in
ascending order.

Input:

{
    's': 2,
    'a': 2,
    'h': 1,
    'd': 1,
    'b': 1,
    'k': 1
}

Output:
{
    'h': 1,
    'd': 1,
    'b': 1,
    'k': 1,
    's': 2,
    'a': 2,
}
'''

from operator import itemgetter

d = {
    's': 2,
    'a': 2,
    'h': 1,
    'd': 1,
    'b': 1,
    'k': 1
}

print(
    dict(
        sorted(
            d.items(),
            key=lambda x: x[1]
        )
    )
)

print(
    dict(
        sorted(
            d.items(),
            key=itemgetter(1)
        )
    )
)
