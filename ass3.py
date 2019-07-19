#PF-Assgn-24
def form_triangle(num1,num2,num3):
    #Do not change the messages provided below
    success="Triangle can be formed"
    failure="Triangle can't be formed"

    if (num1 > num2 + num3):
        return failure
    elif (num2 > num3 + num1):
        return  failure
    elif (num3 > num1 + num2):
        return failure
    else:
        return success
    #Write your logic here

    #Use the following messages to return the result wherever necessary

#Provide different values for the variables, num1, num2, num3 and test your program
num1=3
num2=3
num3=5
message = form_triangle(num1, num2, num3)
print(message)