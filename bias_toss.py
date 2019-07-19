from random import random

def flip(bias):

    return random() < bias

bias = 0.7
count = {False: 0, True: 0}
for i in range(1, 1001):
    toss = flip(bias)
    count[toss] += 1

print("Final result: {} heads, {} tails".format(count[True], count[False]))
