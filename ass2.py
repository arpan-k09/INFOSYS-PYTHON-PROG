#PF-Assgn-23
def calculate_bill_amount(gems_list, price_list, reqd_gems,reqd_quantity):
    bill_amount=0

    count = 0

    merge_list = []
    while count != 5:
        merge_list = merge_list + [[gems_list[count]]+[price_list[count]]]
        count = count + 1

    le =len(reqd_gems)
    lenr = 0
    req_list = []

    while lenr != le :
        req_list = req_list + [[reqd_gems[lenr]]+[reqd_quantity[lenr]]]
        lenr = lenr + 1

    lenr = 0
    price = 0
    while lenr != le :
        count1 = 0
        mcount = len(merge_list)
        qua = req_list[lenr][1]

        reqg = req_list[lenr][0]

        while count1 != mcount:

            ml = merge_list[count1][0]

            if reqg == ml :
                row_price = merge_list[count1][1]
                #print(row_price)
                price = price + (row_price*qua)
                break

            count1 = count1 + 1
        lenr = lenr + 1

    if price >= 30000.0 :
        price = price*0.95
    elif price < 30000.0:
        price = price
    else:
        print("Gems not available")

    bill_amount = price


    #Write your logic here
    return bill_amount


#List of gems available in the store
gems_list=["Emerald","Ivory","Jasper","Ruby","Garnet"]

#Price of gems available in the store. gems_list and price_list have one-to-one correspondence
price_list=[1760,2119,1599,3920,3999]

#List of gems required by the customer
reqd_gems=["Ivory","Emerald","Garnet"]

#Quantity of gems required by the customer. reqd_gems and reqd_quantity have one-to-one correspondence
reqd_quantity=[3,10,12]

bill_amount=calculate_bill_amount(gems_list, price_list, reqd_gems, reqd_quantity)
print(bill_amount)