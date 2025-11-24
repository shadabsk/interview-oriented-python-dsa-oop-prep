'''
n = 6 --> [0, 1, 1, 2, 3, 5] --> 0 + 1 + 1 + 2 + 3
'''

n = 6

fibo_ser_list = [0, 1]

while len(fibo_ser_list) < n:
    fibo_ser_list.append(
        fibo_ser_list[-1] + fibo_ser_list[-2]
    )

print(fibo_ser_list)


# fibonacci using function and conditions

def generate_finbonacci(n):
    fibo_ser_list = [0, 1]

    if n <= 0:
        return []
    elif n == 1:
        return [0]
    elif n == 2:
        return fibo_ser_list
    else:
        while len(fibo_ser_list) < n:
            fibo_ser_list.append(
                fibo_ser_list[-1] + fibo_ser_list[-2]
            )

    return fibo_ser_list


print(generate_finbonacci(6))



# fibonacci using function and conditions
def generate_finbonacci_using_recursion(n):
    fibo_ser_list = [0, 1]

    if n <= 0:
        return []
    elif n == 1:
        return [0]
    elif n == 2:
        return fibo_ser_list
    else:
        '''
        '6 -> 5' => [0, 1, 1, 2, 3, 5]
        '5 -> 4' => [0, 1, 1, 2, 3]
        '4 -> 3' => [0, 1, 1, 2]
        '3 -> 2' => [0, 1, 1]
        '''
        fibo_ser_list = generate_finbonacci_using_recursion(n - 1)
        fibo_ser_list.append(
            fibo_ser_list[-1] + fibo_ser_list[-2]
        )

    return fibo_ser_list


print(generate_finbonacci_using_recursion(6))