#PF-Assgn-35

#Global variable
list_of_marks=(12,18,25,24,2,5,18,20,20,21)


def sort_marks(list_of):
    return sorted(list_of)


def find_more_than_average(list_of):

    sum = 0
    leng = len(list_of)
    count = 0

    while count != leng:
        n = list_of[count]
        sum = sum + n
        count = count + 1

    avg = sum/leng
    li = []
    count1 = 0
    while count1 != leng:
        n = list_of[count1]
        if n>avg :
            li = li + [n]
        count1 = count1 + 1
    final_list = tuple(li)

    le = len(final_list)
    per = (le/leng)*100
    return per

def generate_frequency(list_of):

    count = 0

    leng = len(list_of)
    final_li = [] * 25
    count2 = 0

    while count2 != 25:
        final_li = final_li +[0]
        count2 = count2 + 1

    n = list_of[count]
    print(n)
    n1 = 0
    while count != leng:
        n = list_of[count]
        print(n)
        n1 = final_li[n]
        print(n1)

        if n1 > 0:
            n1 = n1 + 1
        else:
            n1 = 1

        final_li.insert(n,n1)

        count = count + 1

    return final_li



print(find_more_than_average(list_of_marks))
print(generate_frequency(list_of_marks))


print(sort_marks(list_of_marks))