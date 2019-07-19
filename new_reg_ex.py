#PF-Assgn-53
#This verification is based on string match.
import re
poem="It takes strength for being certain,\nIt takes courage to have doubt.\nIt takes strength for challenging alone,\nIt takes courage to lean on another.\nIt takes strength for loving other souls,\nIt takes courage to be loved.\nIt takes strength for hiding our own pain,\nIt takes courage to help if it is paining for someone."
def found_number(p):
    count = p.count("v")
    return count
#Note: Triple quotes can be used to enclose Strings which has lines of text.

print(found_number(poem),"\n")

#Write your logic here for question 1
print(re.sub(r"\n",r" ",poem),"\n")
po = str(re.sub(r"co",r"Co",poem))
print(re.sub(r"ch",r"Ch",po),"\n")
#print(#Write your regular expression here for question 2)

po = str(re.sub(r"ai...",r"ai*\*",poem))
print(re.sub(r"hi...",r"hi*\*",po))
'''print()
print(#Write your regular expression here for question 3)

print()
print(#Write your regular expression here for question 4)'''