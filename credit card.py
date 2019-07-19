#PF-Assgn-58
def validate_credit_card_number(card_number):
    #start writing your code here
    leng = len(str(card_number))
    count = 0
    res = list(map(int, str(card_number)))
    sum = 0
    while count < leng:

        nu = res[count]
        mul = nu*2
        if mul>9:
            rem = mul%10
            rev = mul//10
            mul = rem+rev
        sum = sum + mul

        count = count + 2

    count1 = 1
    sum1 = 0
    while count1 < leng:
        sum1 = sum + res[count1]
        count1 = count1 + 2

    total_sum = sum + sum1
    if (total_sum%10)==0:
        return True
    else:
        return False



card_number= 1456734512345698 #4539869650133101  #1456734512345698 # #5239512608615007
result=validate_credit_card_number(card_number)
if(result):
    print("credit card number is valid")
else:
    print("credit card number is invalid")