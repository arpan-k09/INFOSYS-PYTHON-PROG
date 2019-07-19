#PF-Assgn-52

#This verification is based on string match.

def sum_of_numbers(list_of_num,filter_func=None):
    sum = 0
    leng = len(list_of_num)
    count = 0
    count1 = 0

    if filter_func == None:
        while count != leng:
            w = list_of_num[count]
            sum = sum + w
            count = count + 1
    else:
        final_list = filter_func(list_of_num)
        leng1 = len(final_list)
        while count1 != leng1:
            w = final_list[count1]
            sum = sum + w
            count1 = count1 + 1

    return sum

def even(data):
    leng = len(data)
    count = 0
    final_list = []
    while count != leng:
        if (data[count]%2) == 0:
            final_list = final_list + [data[count]]
        count = count + 1
    return final_list

def odd(data):
    leng = len(data)
    count = 0
    final_list = []
    while count != leng:
        if (data[count] % 2) != 0:
            final_list = final_list + [data[count]]
        count = count + 1
    return final_list



sample_data = range(1,11)
final_data = list(sample_data)


print(sum_of_numbers(final_data,None))
print(sum_of_numbers(sample_data,odd))