'''
You are given a string consisting of lowercase alphabetic characters.
Your task is to identify all maximal contiguous substrings
where no character repeats within that substring.

Return the list of these unique-character substrings in the order they appear.

A substring ends as soon as a character repeats, and a new substring
begins from the repeated character.

Example

Input:
"abcddefxyz"

Output:
["abcd", "defxyz"]

Explanation:
"abcd" → all characters are unique
Repetition of 'd' breaks the sequence

Next unique sequence is "defxyz"
'''


def find_max_unique_sequence_in_str(input_str):
    stack = []
    result_list = []

    for val in input_str:
        if val not in stack:
            stack.append(val)
        else:
            cur_unique_seq = "".join(stack)
            if cur_unique_seq not in result_list:
                result_list.append(cur_unique_seq)
            stack = [val]

    if stack:
        cur_unique_seq = "".join(stack)
        if cur_unique_seq not in result_list:
            result_list.append(cur_unique_seq)

    return len(sorted(result_list)[-1])


input_str = "abcddefxyz"

print(
    find_max_unique_sequence_in_str(input_str)
)
