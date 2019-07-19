# PF-Tryout
import re

flight_details = "Good Evening, Welcome to British Airways. Your flight number is ba8004. Flight departure time is 16:45"


# This function returns the values in the search result
def printout(search_result):
    if (search_result != None):
        return search_result.group()
    else:
        return "No Output"



search_result = re.search(r"British Airways",flight_details)
# Write your regular expression here for question 1
# This will invoke the printout() and displays the search result values
print(printout(search_result))

search_result = re.search(r"\d{2}:\d{2}$",flight_details)
print(printout(search_result))

search_result = re.search(r"^Good",flight_details)
print(printout(search_result))

search_result = re.search(r"F.....",flight_details)
print(printout(search_result))


print(re.sub(r"ba(\d{4})",r"BA\1",flight_details))
