#PF-Assgn-31
def check_palindrome(word):
    str1 = word
    str2 = "".join(reversed(str1))
    print(str2)
    if str1==str2:
        return True
    else:
        return False


status=check_palindrome("malayalam")
if(status):
    print("word is palindrome")
else:
    print("word is not palindrome")