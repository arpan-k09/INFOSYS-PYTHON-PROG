#PF-Assgn-38

def check_double(number):
    n1 = number * 2
    l1 = str(number)
    l2 = str(n1)
    comp = set(l1)
    comp1 = set(l2)
    s3 = comp&comp1
    if len(l1) == len(l2):
        if len(comp) == len(s3):
            return True
        else:
            return False
    else:
        return False

#Provide different values for number and test your program
print(check_double(125874))