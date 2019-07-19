def find_leap_years(given_year):
    count = 1 
    w = given_year
    ye = given_year
    while w == 0:
        if (ye%4 == 0):
            w = ye
        else:
            ye = ye + 1
    print(ye)
    year_list = [ye]

    print(year_list)
    year_list = year_list + [year_list[count-1]+4]
    x=[year_list[count-1]]
    print(year_list)
    # Write your logic here
    print(x)
    return year_list

list_of_leap_years=find_leap_years(2000)