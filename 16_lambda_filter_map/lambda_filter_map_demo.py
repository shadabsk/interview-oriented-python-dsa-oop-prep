'''
Use basic lambda expression to compute square of list -> [2, 4] => [4, 8]
Use filter to get even numbers from a list -> [1, 2, 3, 4, 5] => [2, 4]

Combine lambda and filter with map to achieve the same
'''

# lambda example
y = lambda x: x**2

sample_input_list = [2, 4]

print(list(map(y, sample_input_list)))


# better way to write above expression

sample_input_list = [2, 4]

print(
    list(
        map(
            lambda x: x**2, sample_input_list
        )
    )
)


# filter

sample_input_list = [1, 2, 3, 4, 5]

print(
    list(
        filter(
            lambda x: x % 2 == 0,
            sample_input_list
        )
    )
)

print(
    list(
        map(
            lambda x: x,
            filter(
                lambda x: x % 2 == 0,
                sample_input_list
            )
        )
    )
)
