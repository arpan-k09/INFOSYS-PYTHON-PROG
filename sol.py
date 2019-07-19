def find_leap_years(given_year):
    count = 1
    w = 0
    ye = given_year
    while w == 0:
        if (ye % 4 == 0):
            w = ye
        else:
            ye = ye + 1
    print(ye)
    year_list = [ye]

    while count != 15:
        year_list = year_list + [year_list[count - 1] + 4]
        count = count + 1
    # Write your logic here

    return year_list


list_of_leap_years = find_leap_years(2000)
print(list_of_leap_years)