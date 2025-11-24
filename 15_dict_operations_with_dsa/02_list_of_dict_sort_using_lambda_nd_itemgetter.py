'''
Given a list of dictionary, get the product having maximum rating

Input:

[
    {
        'product_name': 'xyz',
        'rating': 2,
    },
    {
        'product_name': 'xyz',
        'rating': 5,
    },
    {
        'product_name': 'xyz',
        'rating': 1,
    },
]

Output:
xyz
'''

from operator import itemgetter

input_list = [
    {
        'product_name': 'xyz',
        'rating': 2,
    },
    {
        'product_name': 'xyz',
        'rating': 5,
    },
    {
        'product_name': 'xyz',
        'rating': 1,
    },
]

print(
    sorted(
        input_list,
        key=itemgetter('rating'),
        reverse=True
    )[0]['product_name']
)


print(
    sorted(
        input_list,
        key=lambda x: x['rating'],
    )[-1]['product_name']
)
