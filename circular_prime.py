BAKI CHE





#PF-Assgn-57
def check_prime(number):
    #remove pass and write your logic here. if the number is prime return true, else return false
    count = 2
    while count != number:
        if (number%count)==0:
            return False
        count = count + 1
    return True

def rotations(num):
    #remove pass and write your logic here. It should return the list of different combinations of digits of the given number.
	#Rotation should be done in clockwise direction. For example, if the given number is 197, the list returned should be [197, 971, 719]
    n = num
    rem = 0
    rev = 0
    final = 0

    flag = check_prime(n)
    if flag == True:
        new_num = 0
        while flag==True:
            rem = n%10
            rev = n//10
            if num>99 and num<1000:
                new_num = (rem*100)+rev
                n = new_num
                flag = check_prime(new_num)
            elif num>9 and num<100:
                new_num = (rem*10)+rev
                n = new_num
                flag = check_prime(new_num)
            else:
                flag = check_prime(n)

            if flag == False:
                return False


def get_circular_prime_count(limit):
    l = limit
    count = 2

    while count != l:
        if rotations(count):
            print(count)
        count = count + 1

#Provide different values for limit and test your program
print(get_circular_prime_count(1000))