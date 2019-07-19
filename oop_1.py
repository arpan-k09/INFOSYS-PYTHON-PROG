# OOPR-Exer-1
def purchase_mobile(price,mobile_brand):
    product_type = "Mobile"
    if mobile_brand == "Apple":
        discount = 10
    else:
        discount = 5
    total_price = price - price * discount / 100
    print("Total price of " + product_type + " is " + str(total_price))

def purchase_shoe(price,material) :
    product_type = "Shoe"
    if material == "leather":
        tax = 5
    else:
        tax = 2
    total_price = price + price * tax / 100
    print("Total price of " + product_type + " is " + str(total_price))







purchase_mobile(20000, "Apple")
purchase_shoe( 200, "leather")

