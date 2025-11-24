'''
Given an input string, find whether its palindrome or not

Example 1:
aabbaa

Output:
True

Example 2:
shadabsk

Output:
False
'''


def check_is_palindrome(input_str):
    reversed_str = ""
    for char in input_str:
        reversed_str = char + reversed_str

    return reversed_str == input_str


input_str = "shadabsk"
print(
    check_is_palindrome(input_str)
)

input_str = "aabbaa"
print(
    check_is_palindrome(input_str)
)
