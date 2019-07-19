#PF-Exer-26
import math

def factorial(number):
    sum = 0
    if number == 0:
        return 1
    else:
        while number != 0:
            rem = number % 10
            sum = sum + math.factorial(rem)
            number = number//10

    return sum


def find_strong_numbers(num_list):
    final_list = []
    leng = len(num_list)
    count = 0
    while count != leng :
        num = num_list[count]
        rm = factorial(num)

        if num == rm :
            final_list = final_list + [rm]



        count = count + 1
    return final_list

num_list=[145,375,100,2,10]
strong_num_list = find_strong_numbers(num_list)
print(strong_num_list)