#PF-Exer-38
#This verification is based on string match.
import math
num1=36
num2=7
num3=18

calc = lambda x,y: (x%y)+(x-y)
print(calc(num1,num2))

square_root = lambda x : math.sqrt(x)#Write the lambda expression for question2
print(square_root(num3))

square_root2= lambda x : x**0.5#Write the lambda expression for question3
print(square_root2(num3))

