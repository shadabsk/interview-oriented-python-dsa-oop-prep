'''
a = "34"; b = "7"

Expected Output: "238"

Explanation:
[0,2,8]
[2,1,0]
=
[2,3,8]
'''

a = "34"
b = "7"

li = [
    int(a[0]), int(a[1])
]
ri = [
    int(b[0])
]

lir = [0]
rir = [0]

for i in reversed(li):
    for j in reversed(ri):
        result = i*j

        while result > 0:
            last_digit = result % 10
            result //= 10

            if len(lir) < 3:
                lir.insert(1, last_digit)
            else:
                rir.insert(0, last_digit)


print(
    "".join(
        map(
            str, [x+y for x, y in zip(lir, rir)]
        )
    )
)
