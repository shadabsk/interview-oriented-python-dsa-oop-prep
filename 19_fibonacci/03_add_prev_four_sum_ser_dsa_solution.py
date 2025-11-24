'''
n= 6 --> [1, 2, 3, 4, 10, 19]
'''

fibo_four_series = [1, 2, 3, 4]
n = 6
while len(fibo_four_series) < n:
    fibo_four_series.append(
        sum(fibo_four_series[-4:])
    )

print(fibo_four_series)
