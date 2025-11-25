'''
You are given an array of integers representing cards, where each card’s
value may be positive or negative.
Your task is to determine the maximum score you can obtain by picking
any contiguous subarray of cards.

The score is defined as the sum of the values of the picked cards.

Return the maximum possible sum.

Example

Input:
[4, -4, 1, -3, 1, -3]

Output:
5

Explanation:
The maximum score is achieved by picking only the card [4]
or equivalently choosing the empty sequence from negatives and then
picking 4 + 1 = 5 by combining best positive contributions.
The best possible sum is 5.
'''


def find_cur_max_card_picked(cur_card_list):
    power_sum = 0
    max_card_picked = 0

    for card in cur_card_list:
        if card + power_sum >= 0:
            power_sum += card
            max_card_picked += 1

    return max_card_picked


def get_max_card_picked(card_list):
    result_list = []
    for idx, _ in enumerate(card_list):
        cur_card_list = card_list[:idx] + card_list[idx + 1:]
        result_list.append(
            find_cur_max_card_picked(cur_card_list)
        )

    print(result_list)
    return sorted(result_list)[-1]


card_list = [4, -4, 1, -3, 1, -3]

print(
    get_max_card_picked(card_list)
)
