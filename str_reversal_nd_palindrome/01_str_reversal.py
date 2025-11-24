'''
Given input -> shadabsk
perform string reversal -> ksbadahs
'''

input_str = "shadabsk"
reverse_str = ""

for char in input_str:
    # 's' -> 'hs' -> 'ahs'
    reverse_str = char + reverse_str

print(reverse_str)

print(input_str[::-1])
