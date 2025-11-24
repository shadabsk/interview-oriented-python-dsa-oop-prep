'''
You are given a list of strings.
Two strings are considered anagrams if they contain the same characters
in the same quantities, but possibly in a different order.

Your task is to group all anagrams together.
Strings that are anagrams of each other must appear in the same group.
Strings with no anagram pair should appear as a single-element group.

Return the list of grouped anagrams, preserving the relative order of first
appearance of each group.

Example

Input:
["bat", "tab", "ate", "tea", "x"]

Output:
[["bat", "tab"], ["ate", "tea"], ["x"]]

Explanation:

"bat" and "tab" contain the same characters → group together
"ate" and "tea" are also anagrams → group together
"x" has no anagram → appears alone
'''

from collections import defaultdict

result_list = defaultdict(list)

input_list = ["bat", "tab", "ate", "tea", "x"]

for word in input_list:
    # for bat -> ['a', 'b', 't']
    key = "".join(sorted(list(word)))
    result_list[key].append(word)

print(list(result_list.values()))


# Without using defaultdict
result_dict = {}

input_list = ["bat", "tab", "ate", "tea", "x"]

for word in input_list:
    # for bat -> ['a', 'b', 't']
    key = "".join(sorted(list(word)))

    if key not in result_dict:
        result_dict[key] = []

    result_dict[key].append(word)

print(list(result_dict.values()))
