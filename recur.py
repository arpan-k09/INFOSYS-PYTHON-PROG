#PF-Exer-32

def human_pyramid(no_of_people):
    if (no_of_people == 1):
        return 1 * (50)
    else:
        return no_of_people * (50)

def find_maximum_people(max_weight):
    no_of_people=1
    weight = 0
    while weight < max_weight:
        human_pyramid(no_of_people) + human_pyramid(no_of_people + 2)

    return no_of_people

#Provide different values for max_weight and test your program
max_people=find_maximum_people(1000)
print(max_people)