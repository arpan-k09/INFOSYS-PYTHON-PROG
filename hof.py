#PF-Exer-41
#This verification is based on string match.

def sum_all(function, data):
    sum = 0
    leng = len(data)
    count = 0
    while count != leng:
        w = data[count]
        if(function(w)):
           sum = sum + w
        count = count + 1

    return sum

list_of_nos=[100,200,300,500,1040]
greater = lambda no: no>10

divide = lambda  no: (no%10)==0 and no <=100

range_of_values = lambda no: no >= 25 and no <= 50

#Use the below given print statements to display the output
# Also, do not modify them for verification to work
print(sum_all(greater,list_of_nos))
print(sum_all(divide,list_of_nos))
print(sum_all(range_of_values,list_of_nos))