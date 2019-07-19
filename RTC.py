#PF-Assgn-29
def calculate(distance,no_of_passengers):
    ppl = 70
    kmpl = 10
    ppt = 80

    total_cost = ppl * (distance/10)
    ticket = ppt * no_of_passengers

    if total_cost > ticket:
        return -1
    else:
        return (ticket - total_cost)



#Provide different values for distance, no_of_passenger and test your program
distance=20
no_of_passengers=50
print(calculate(distance,no_of_passengers))