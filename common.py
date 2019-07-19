#PF-Assgn-33

def find_common_characters(msg1,msg2):

    s = set(msg1)
    s1 = set(msg2)

    s3 = s & s1

    print(s3)

    str1 = "".join(s3)
    print(str1)

    if len(str1) > 0:
        return str1
    else:
        return -1

#Provide different values for msg1,msg2 and test your program
msg1="Python"
msg2="python"
common_characters=find_common_characters(msg1,msg2)
print(common_characters)