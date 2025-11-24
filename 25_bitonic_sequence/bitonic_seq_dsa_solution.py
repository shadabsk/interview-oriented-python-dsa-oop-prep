'''
You are given an array of integers.
Your task is to partition the array into non-overlapping, maximal,
contiguous bitonic sequences.

A bitonic sequence is defined as a contiguous subarray that is either:
strictly increasing, or
strictly decreasing, or
strictly increasing and then strictly decreasing.

Output
Return the list of all such maximal bitonic segments in the order they appear.

Example

Example

Input:
[10, 8, 9, 12, 15, 6, 7]

Output:
[[10, 8], [8, 9, 12, 15, 6], [6, 7]]

Explanation:

[10, 8] is strictly decreasing, and the trend reverses at 8 → 9.

From 8, the sequence increases up to 15 and then decreases to 6, so the
next bitonic segment is [8, 9, 12, 15, 6].

Trend changes again at 6 → 7, forming the final increasing segment [6, 7].
'''


def generate_bitonic_sequence(input_list):
    stack = []
    result_list = []
    p_set = set()

    for idx, cur_elem in enumerate(input_list):
        if idx in p_set:
            continue

        # incrementing sequence
        if stack and cur_elem >= stack[-1]:
            stack.append(cur_elem)
            p_set.add(idx)
        else:
            stack.append(cur_elem)
            p_set.add(idx)

            inner_list = input_list[idx+1:]
            c_idx = idx

            for i_val in inner_list:
                # decrementing sequence
                if i_val <= stack[-1]:
                    c_idx += 1
                    p_set.add(c_idx)
                    stack.append(i_val)
                else:
                    break

            result_list.append(stack)
            stack = [input_list[c_idx]]

    if stack and stack not in result_list:
        result_list.append(stack)
    return result_list


input_list = [10, 8, 9, 12, 15, 6, 7]
print(
    generate_bitonic_sequence(
        input_list
    )
)
