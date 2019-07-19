#PF-Assgn-59
def check_perfect_number(number):
    #start writing your code here
    n = number
    count = 1
    sum = 0
    while count != n:
        if (n%count) == 0:
            sum = sum + count
        count = count + 1
    if sum == n:
        return True
    else:
        return False

def check_perfectno_from_list(no_list):
    #start writing your code here
    final_list = []
    for x in no_list:
        flag = check_perfect_number(x)
        if flag == True:
            final_list = final_list + [x]

    return final_list


perfectno_list=check_perfectno_from_list([18,6,4,2,1,28])
print(perfectno_list)