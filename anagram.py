#PF-Assgn-54
def check_anagram(data1,data2):
    leng1 = len(data1)
    leng2 = len(data2)
    count1 = 0
    count2 = 0
    list1 = []
    list2 = []
    while count1 != leng1:
        list1 = list1 + [data1[count1]]
        count1 = count1 + 1
    print(list1)
    while count2 != leng2:
        list2 = list2 + [data2[count2]]
        count2 = count2 + 1
    print(list2)

    count3 = 0
    set1 = set(list1)
    set2 = set(list2)

    set3 = set1-set2
    len(set3)
    a = 0
    if  a > 0:
        flag = False
        return False
    else:
        while count3 != len(set1):
            if list1[count3] == list2[count3]:
                flag = False
            else:
                flag = True

            if flag == False:
                return False

            count3 = count3 + 1

        return flag

print(check_anagram("eat","tea"))
#print(check_anagram("backward","drawback"))