#PF-Assgn-56

def max_frequency_word_counter(data):
    word=""
    frequency=0

    count = 0
    li = data.split(" ")
    leng = len(li)

    final_list = []

    while count != leng:
        num = li.count(li[count])
        name = li[count]
        str1 = str(num)+":"+name
        final_list = final_list + [str1]

        count = count + 1

    final_list.sort(reverse=True)

    word_list = []
    frequency_list = []
    for i in final_list:
        string_list=i.split(":")
        word_list = word_list + [string_list[1]]
        frequency_list = frequency_list + [string_list[0]]
    count1 = 0
    final_len = len(word_list)
    frequency = frequency_list[count1]
    while frequency == frequency_list[count1]:
        name = word_list[count1]
        name1 = word_list[count1+1]
        freq = frequency_list[count1]
        freq1 = frequency_list[count1+1]
        if freq == freq1:
            if name == name1:
                word = name
                frequency = freq
            elif len(name)>len(name1):
                word = name
                frequency = freq
            else:
                word = name1
                frequency = freq1
        elif freq > freq1:
            word = name
            frequency = freq
        else:
            word = name1
            frequency =freq1
        count1 = count1 + 1
    print(word,frequency)




    return final_list
    #start writing your code here
    #Populate the variables: word and frequency


    # Use the below given print statements to display the output
    # Also, do not modify them for verification to work
    #print(word,frequency)


#Provide different values for data and test your program.
data="Work like you do not need money, love like you have never been hurt, and dance like no one is watching"
max_frequency_word_counter(data)