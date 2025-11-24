'''
You are given a noisy string, with the expection of achieving cleaned output
in the sorted order

Noisy str input -> "MR', ['CT', 'MR'], 'FP', 'MR'"

Expected output -> ['CT', 'MR', 'FP']
'''

NOISY_CORPUS_LIST = ['\'', '[', ']']

input_str = "MR', ['CT', 'MR'], 'FP', 'MR'"

first_pass_processed =  "".join(
    [char.strip() for char in input_str if char not in NOISY_CORPUS_LIST]
)

print(
    sorted(
        list(
            set(
                first_pass_processed.split(',')
            )
        )
    )
)
