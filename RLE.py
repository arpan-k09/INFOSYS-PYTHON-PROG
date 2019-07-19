#PF-Assgn-30

def encode(message):

   st = message
   str1 = ""
   length = len(st)

   while length != 0:
       count = 0
       while st[count]==st[count+1]:
           count = count + 1
           length = length - 1
            str1 = str(count+1)+st[count]





#Provide different values for message and test your program
encoded_message=encode("ABBBBCCCCCCCCAB")
print(encoded_message)