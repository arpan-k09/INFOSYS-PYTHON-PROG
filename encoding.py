#PF-Assgn-50

def sms_encoding(data):
    #start writing your code here
    list_of = list(data.split(" "))

    count = 0
    length = len(list_of)
    final_list = []
    vowel = {"A","E","I","O","U","a","e","i","o","u"}
    while count != length:
        name = list_of[count]
        leng = len(name)
        if leng == 1:
            if(name == "A" or name == "E" or name == "I" or name == "O" or name == "U"or name == "a"or name == "e"or name == "i" or name == "o"or name == "u"):
                final_list = final_list + [name]
        else:
            count_name = 0
            final_name = []
            while count_name != leng:
                n = name[count_name]
                if  not (n == "A" or n == "E" or n == "I" or n == "O" or n == "U"or n == "a"or n == "e"or n == "i" or n == "o" or n == "u"):
                    final_name = final_name + [n]


                count_name = count_name + 1
            st = "".join(final_name)
            print(st)
            final_list = final_list + [st]
        count = count + 1


    final__str = " ".join(final_list)
    return final__str
data="I love Python"
print(sms_encoding(data))