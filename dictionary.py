#PF-Assgn-48

def find_correct(word_dict):
    #start writing your code here
    key_list = []
    value_list = []

    for x in word_dict:
        key_list = key_list + [x]
    for x in word_dict:
        value_list = value_list + [word_dict.get(x)]

    correct = 0
    almost_correct = 0
    wrong = 0
    count = 0
    key = ""
    value = ""
    while count != len(key_list):
        count1 = 0
        diff = 0
        key = key_list[count]
        value = value_list[count]

        le_key = len(key)
        le_val = len(value)

        while count1 != le_key:
            if key[count1] != value[count1]:
                diff = diff + 1

            count1 = count1 + 1

        if key == value:
            correct = correct + 1
        elif le_key != le_val or diff > 2:
            wrong = wrong + 1
        else:
            almost_correct = almost_correct + 1



        count = count + 1

    final_list = [correct] + [almost_correct] + [wrong]
    return final_list


word_dict = {'CHECK': 'CHEK', 'RADIO': 'RADICAL', MIND: MUND, VENDOR: VENDING, ALWAYS: ALLISWELL}
#word_dict={"THEIR": "THEIR","BUSINESS":"BISINESS","WINDOWS":"WINDMILL","WERE":"WEAR","SAMPLE":"SAMPLE"}
print(find_correct(word_dict))