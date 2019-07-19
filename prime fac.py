#PF-Assgn-42
def find_f(num):
    li = []
    for i in range(2, num + 1):
        if (num % i == 0):
            isprime = 1
            for j in range(2, (i // 2 + 1)):
                if (i % j == 0):
                    isprime = 0
                    break

            if (isprime == 1):
                li = li + [i]

        i = i + 1
    m = max(li)

    return m


def find_g(num):
    n = num
    sum = 0
    count = 0
    while count != 9:

        s = find_f(n)
        sum = sum + s
        n = n + 1
        count = count + 1
    return sum



print(find_g(10))








