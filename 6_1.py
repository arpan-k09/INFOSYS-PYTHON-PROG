#PF-Assgn-40
def is_palindrome(word):
    s = word.lower()
    string = "".join(reversed(s))
    if string == s:
        return True
    else:
        return False
#Provide different values for word and test your program
result=is_palindrome("MadAMa")
print(result)
if(result):
    print("The given word is a Palindrome")
else:
    print("The given word is not a Palindrome")