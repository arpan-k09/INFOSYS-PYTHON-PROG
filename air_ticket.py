#PF-Assgn-55

#Sample ticket list - ticket format: "flight_no:source:destination:ticket_no"
#Note: flight_no has the following format - "airline_name followed by three digit number

#Global variable
ticket_list=["AI567:MUM:LON:014","AI077:MUM:LON:056", "BA896:MUM:LON:067", "SI267:MUM:SIN:145","AI077:MUM:CAN:060","SI267:BLR:MUM:148","AI567:CHE:SIN:015","AI077:MUM:SIN:050","AI077:MUM:LON:051","SI267:MUM:SIN:146"]

def find_passengers_flight(airline_name="AI"):
    #This function finds and returns the number of passengers travelling in the specified airline.
    count=0
    for i in ticket_list:
        string_list=i.split(":")
        if(string_list[0].startswith(airline_name)):
            count+=1
    return count

def find_passengers_destination(destination):
    #Write the logic to find and return the number of passengers traveling to the specified destination
    count = 0
    for i in ticket_list:
        string_list = i.split(":")
        if (string_list[2].startswith(destination)):
            count += 1
    return count

def find_passengers_per_flight():
    '''Write the logic to find and return a list having number of passengers traveling per flight based on the details in the ticket_list
    In the list, details should be provided in the format:
    [flight_no:no_of_passengers, flight_no:no_of_passengers, etc.].'''
    airline_list = []
    total_list = []
    for i in ticket_list:
        string_list=i.split(":")
        airline_list = airline_list + [string_list[0]]
        total_list = total_list + [string_list[0]]
    airline_list = list(set(airline_list))

    final_len = len(airline_list)
    count = 0
    out_list = []
    final_out = []
    while count != final_len:
        count1 = 0
        sum = 0
        out_list = []
        name = airline_list[count]
        total = len(total_list)
        while count1 != total :
            all_name = total_list[count1]
            if name == all_name:
                sum = sum + 1
            count1 = count1 + 1
        str1 = str(sum)+":"+airline_list[count]
        out_list = out_list + [str1]
        final_out = final_out + out_list

        count = count + 1
    return final_out




def sort_passenger_list():
    #Write the logic to sort the list returned from find_passengers_per_flight() function in the descending order of number of passengers
    out = find_passengers_per_flight()
    out.sort(reverse=True)

    num = []
    for i in out:
        string_list = i.split(":")
        str1 = string_list[1]+":"+str(string_list[0])
        num = num + [str1]

    return num


#Provide different values for airline_name and destination and test your program.
print(find_passengers_flight("AI"))
print(find_passengers_destination("LON"))

print(sort_passenger_list())