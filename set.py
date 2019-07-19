# PF-Exer-23
def translate(bilingual_dict, english_words_list):
    # Write your logic here

    len_of_list = len(english_words_list)
    count = 0
    str_index = ""
    swedish_words_list = []
    while count != len_of_list:

        list1 = english_words_list[count]

        for x in bilingual_dict:
            str_index = x

            if list1 == str_index:
                swedish_words_list = swedish_words_list + [bilingual_dict[str_index]]
                break

        count = count + 1

    return swedish_words_list


bilingual_dict = {"merry": "god", "christmas": "jul", "and": "och", "happy": "gott", "new": "nytt", "year": "ar"}
english_words_list = ["merry", "christmas"]
print("The bilingual dict is:", bilingual_dict)
print("The english words are:", english_words_list)

swedish_words_list = translate(bilingual_dict, english_words_list)
print("The equivalent swedish words are:", swedish_words_list)