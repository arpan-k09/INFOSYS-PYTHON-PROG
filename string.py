# PF-Exer-22

def generate_ticket(airline, source, destination, no_of_passengers):
    ticket_number_list = []
    # Write your logic here

    li = ""
    ticket_number = 101
    li = airline
    source = source[:3]
    destination = destination[:3]
    count = 1

    li = li + ":" + source + ":" + destination
    print(li)
    li0 = li + ":" + str(ticket_number)
    print(li0)
    ticket_number_list = ticket_number_list + [li0]
    print(ticket_number_list)

    while count != no_of_passengers:
        li1 = li
        ticket_number = ticket_number + 1
        li1 = li1 + ":" +str(ticket_number)
        ticket_number_list = ticket_number_list + [li1]
        count = count + 1




        # Use the below return statement wherever applicable
    return ticket_number_list


# Provide different values for airline,source,destination,no_of_passengers and test your program
#list_t = []
print(generate_ticket("AI", "Bangalore", "London", 7))
#print(list_t)
