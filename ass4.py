#PF-Assgn-28

def find_max(num1, num2):
    max_num=-1
    # Write your logic here
    sum = 0

    list_number = []

    while num1 != num2 :

        list_number = list_number + [num1]

        num1 = num1 + 1
    list_number = list_number + [num2]

    count = 0
    leng = len(list_number)

    list_number1 = []
    while count != leng:
        n = list_number[count]
        n1 = n

        sum = 0
        while n != 0:
            rem = n % 10

            sum = sum + rem
            n = (int)(n / 10)



        if (sum % 3) == 0:
            if (n1 > 9 and n1 < 100):
                if (n1 % 5) == 0:
                    list_number1 = list_number1 + [n1]
                else:
                    print("Number is no multiple of 5")
                    max_num = -1
            else:
                print("Number is not two digits")
                max_num = -1
        else:
            print("Sum of digit of number is not multiple of 3")
            max_num = -1


        count = count + 1





    max_num = max(list_number1)
    if max_num > 0 :
        return max_num
    else:
        max_num = -1
        return  max_num
#Provide different values for num1 and num2 and test your program.
max_num=find_max(15,20)
print(max_num)