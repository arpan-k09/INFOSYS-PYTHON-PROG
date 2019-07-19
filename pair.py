#PF-Assgn-34
def find_pairs_of_numbers(num_list,n):
    count = 0

    length = len(num_list)
    final_count = 0
    while count != (length-1):
        count1 = count + 1
        n1 = num_list[count]
        sum = 0
        while count1 != length:
            sum = n1 + num_list[count1]
            if sum == n :
                final_count = final_count + 1
            count1 = count1 + 1
        count = count + 1



    return final_count


num_list=[1, 2, 4, 5, 6]
n=6
print(find_pairs_of_numbers(num_list,n))