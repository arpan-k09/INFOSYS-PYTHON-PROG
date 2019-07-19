freq = {}
test_str = "Geeks for Geeks"
my_list = []
leng = len(test_str)
count = 0
while(count != leng):
    my_list = my_list + [test_str[count]]
    count = count + 1


#my_list =[1, 1, 1, 5, 5, 3, 1, 3, 3, 1, 4, 4, 4, 2, 2, 2, 2]
for items in my_list:
    freq[items] = my_list.count(items)

freq.pop(" ")
print(freq)
print(sorted(freq.values(),reverse=True))

decy_small = ""
decy_cap = ""

s = [(k, freq[k]) for k in sorted(freq, key = freq.get, reverse=True)]
for k, v in s:
    if k.isupper():
        decy_cap = decy_cap + k
    elif k.islower():
        decy_small = decy_small + k

    print(k, v)
