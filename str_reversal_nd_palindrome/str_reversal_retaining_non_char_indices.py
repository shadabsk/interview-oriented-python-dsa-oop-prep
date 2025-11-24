'''
You are given a string that contains alphabetic characters,
digits, and non-alphabet symbols (such as -, _, /, etc.).

Your task is to:
Reverse only the alphabetic characters in the string
Keep all non-alphabetic characters (digits, dashes, symbols) in
their original positions
Return the resulting transformed string
Non-alphabetic characters must not move.

Example

Input:
"abcd-efg-12-xyz"

Output:
"zyxg-fed-12-cba"
'''

input_str = "abcd-efg-12-xyz"
reverse_str = ""

non_char_index_info_map = {}
for idx, cur_char in enumerate(input_str):
    if (
        ord('a') <= ord(cur_char) <= ord('z') or
        ord('A') <= ord(cur_char) <= ord('Z')
    ):
        reverse_str = cur_char + reverse_str
    else:
        non_char_index_info_map[idx] = cur_char

reverse_str_list = list(reverse_str)
for idx, val in non_char_index_info_map.items():
    reverse_str_list.insert(idx, val)

print(reverse_str)
print(non_char_index_info_map)

print("".join(reverse_str_list))