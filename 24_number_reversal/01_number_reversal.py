'''
Given input -> 1234; perform its reversal -> 4321

r * 10 + l
1234 -> 4 => r = 0 -> 4
123 -> 3 => r = 40 -> 43
12 -> 2 => r = 430 -> 432
1 -> 1 => r = 4320 -> 4321
'''

num = 1234
reverse_num = 0

while num > 0:
    last_digit = num % 10
    reverse_num = reverse_num * 10 + last_digit
    num //= 10

print(reverse_num)
