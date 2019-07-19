#PF-Exer-39
#This verification is based on string match.

principal_amount=4000
duration=12
rate_of_interest=13

simple_interest = lambda p,r,n:(p*r*n)/100#Write the lambda expression here

if(simple_interest(principal_amount,duration,rate_of_interest)>1000):
    print("Platinum Member")
else:
    print("Gold Member")
    #write your logic here