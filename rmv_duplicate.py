#PF-Assgn-60
from collections import OrderedDict
def remove_duplicates(value):
    #start writing your code here
    name = value
    return "".join(OrderedDict.fromkeys(name))


print(remove_duplicates("11223445566666ababzzz@@@123#*#*"))