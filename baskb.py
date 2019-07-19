# PF-Exer-28

# This method accepts the name of winner of each match of the day
def find_winner_of_the_day(*match_tuple):
    team = ""
    count1 = 0
    count2 = 0
    for team in match_tuple:

        if team == "Team1":
            count1 = count1 + 1
        elif team == "Team2":
            count2 = count2 + 1

    if count1 > count2:
        return "Team1"
    elif count2 > count1:
        return "Team2"
    else:
        return "Tie"

# Invoke the function with each of the print statements given below
print(find_winner_of_the_day("Team1","Team2","Team1"))
#print(find_winner_of_the_day("Team1", "Team2", "Team1", "Team2"))
