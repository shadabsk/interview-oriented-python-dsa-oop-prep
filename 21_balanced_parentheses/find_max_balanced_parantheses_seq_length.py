'''
You are given a string consisting only of the characters '(' and ')'.
Your task is to extract all maximal balanced substrings,
where each substring contains properly matched parentheses.

A balanced substring is defined as:

Every opening parenthesis '(' has a corresponding closing parenthesis ')'.

The substring is maximal, meaning it cannot be extended further
without becoming unbalanced.

Return a list of all balanced substrings, in the order they appear
in the input.

Example

Input:
"(()))()()"

Output:
["(())", "()", "()()"]

Explanation:

"(())" is the first maximal balanced segment

"()" is the next balanced segment

"()()" appears at the end and is fully balanced
'''


def find_max_balanced_parantheses(input_str):
    stack = []
    start_ptr = 0
    result_list = []

    for idx, char in enumerate(input_str):
        if char == '(':
            stack.append(char)
        else:
            if stack:
                stack.pop()
                if not stack:
                    result_list.append(
                        input_str[start_ptr:idx+1]
                    )
            else:
                start_ptr = idx + 1
                stack = []

    print(result_list)
    return len(sorted(result_list)[-1])


input_str = '(()))()()'
print(
    find_max_balanced_parantheses(input_str)
)
