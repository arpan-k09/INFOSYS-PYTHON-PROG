#PF-Assgn-37

#Global variables
child_id=(10,20,30,40,50)
chocolates_received=[12,5,3,4,6]

def calculate_total_chocolates(choco):
    leng = len(choco)
    sum = 0
    count = 0
    while count != leng:
        n = choco[count]
        sum = sum + n
        count = count + 1
    return sum



def reward_child(child_id_rewarded,extra_chocolates,choco):


    count = 0
    val = child_id_rewarded

    if extra_chocolates < 1 :
        print("Extra chocolates is less than 1")
    else:
        index = child_id.index(val)

        if index >= 0 :
            n = choco[index] + extra_chocolates

            choco.insert(index,n)

        else:
            print("Child id is invalid")

    print(choco)




    # Use the below given print statements to display the output
    # Also, do not modify them for verification to work

    #print("Extra chocolates is less than 1")
    #print("Child id is invalid")
    #print(chocolates_received)


print(calculate_total_chocolates(chocolates_received))
#Test your code by passing different values for child_id_rewarded,extra_chocolates
reward_child(20,2,chocolates_received)