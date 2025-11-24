'''
You are given two 4-digit positive integers as input.
Your task is to compute their sum and return the result.

Constraints
The system is capable of processing only two numbers at a time.
Each input number must be a 4-digit integer (from 1000 to 9999).
Output must be the correct integer sum.

Example

Input:
9999 + 9999

Output:
19998

 9999
+9999
=
'''

li = [99, 99]
ri = [99, 99]

re = [0] * 4

carry = 0
BASE = 100

while len(li) < 4:
    li.insert(0, 0)
while len(ri) < 4:
    ri.insert(0, 0)

for i in range(3, -1, -1):
    total = li[i] + ri[i] + carry
    carry = total // BASE
    re[i] = total % BASE

print(
    int(
        "".join(
            map(str, re)
        )
    )
)
