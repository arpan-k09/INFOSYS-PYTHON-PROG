# PF-Assgn-44

def find_duplicates(list_of_numbers):
    le = len(list_of_numbers)

    count_first = 0

    final_list = []
    while count_first != (le - 1):
        count_second = count_first + 1
        while count_second != le:
            if list_of_numbers[count_first] == list_of_numbers[count_second]:
                final_list = final_list + [list_of_numbers[count_second]]
            count_second = count_second + 1
        count_first = count_first + 1

    final_set = set(final_list)
    final_list = list(final_set)

    return final_list


list_of_numbers = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4]
list_of_duplicates = find_duplicates(list_of_numbers)
print(list_of_duplicates)