'''
Convert a given binary code -> 101 to its decimal equivalent -> 5

Explanation:

(1 * 2) ** 2 + (0 * 2) ** 1 + (1 * 2) ** 0
'''

sample_input = 101
input_str = str(sample_input)

counter = len(input_str) - 1
decimal_value = 0

for digit in input_str:
    decimal_value += (int(digit) * 2) ** counter
    counter -= 1

print(decimal_value)


decimal_value = 0
for idx, digit in enumerate(reversed(input_str)):
    decimal_value += (int(digit) * 2) ** idx

print(decimal_value)
