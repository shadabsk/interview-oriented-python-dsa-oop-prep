'''
You are given a list of intervals, where each interval is represented
as a pair [start, end] with start <= end.

Two intervals overlap if both of the following conditions hold:
The start of one interval is less than the end of the other (a < d)
The end of one interval is greater than the start of the other (b > c)

Your task is to merge all overlapping intervals and return a list of merged
intervals, sorted by their start values.

Each merged interval must be maximal, meaning it cannot be extended further
by merging with another interval.

Example

Input:
[[1, 3], [2, 4], [7, 8]]

Output:
[[1, 4], [7, 8]]

Explanation:

[1, 3] and [2, 4] overlap because 1 < 4 and 3 > 2, so
they merge into [1, 4]

[7, 8] does not overlap with [1, 4], so it stays as is

Example - II

Input:
[[1, 3], [2, 4], [7, 8], [9, 10], [9, 11]]

Output:
[[1, 4], [7, 8], [9, 11]]
'''


def merge_overlapped_list(sample_input_list):
    first_pass_processed_list = []
    n = len(sample_input_list)
    for idx, _ in enumerate(sample_input_list):
        if idx == n - 1:
            break

        inner_list = sample_input_list[idx] + sample_input_list[idx+1]
        first_pass_processed_list.append(inner_list)

    merged_overlapped_list = []
    processing_list = []

    for val in first_pass_processed_list:
        a, b, c, d = val[0], val[1], val[2], val[3]

        if a < d and b > c:
            cur_combo = [a, d]
            if cur_combo not in processing_list:
                merged_overlapped_list.append(cur_combo)

                processing_list.append(cur_combo)
                processing_list.append([a, b])
                processing_list.append([c, d])
        else:
            if [a, b] not in processing_list:
                merged_overlapped_list.append([a, b])
                processing_list.append([a, b])
            elif [c, d] not in processing_list:
                merged_overlapped_list.append([c, d])
                processing_list.append([c, d])

    duplicated_overlap_dict_info = {}
    for idx, val in enumerate(merged_overlapped_list):
        if val[0] not in duplicated_overlap_dict_info:
            duplicated_overlap_dict_info[val[0]] = []

        duplicated_overlap_dict_info[val[0]].append(idx)

    for _, idx_list in duplicated_overlap_dict_info.items():
        if len(idx_list) > 1:
            for idx in idx_list[:-1]:
                merged_overlapped_list.pop(idx)

    return merged_overlapped_list


sample_input_list = [[1, 3], [2, 4], [7, 8]]
print(
    merge_overlapped_list(sample_input_list)
)

sample_input_list = [[1, 3], [2, 4], [7, 8], [9, 10], [9, 11]]
print(
    merge_overlapped_list(sample_input_list)
)
