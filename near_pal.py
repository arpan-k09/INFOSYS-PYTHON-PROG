def nearest_palindrome(number):
    num = number + 1
    flag = False

    while flag == False:

        str1 = str(num)

        str2 = "".join(reversed(str1))
        num2 = int(str2)

        if num == num2:
            flag = True
            return num
        else:
            flag = False

        num = num + 1
    # start writitng your code here


number = 12300
print(nearest_palindrome(number))