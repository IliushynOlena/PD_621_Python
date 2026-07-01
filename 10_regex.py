import re

str1 = "123"
str2 = "234"
str3 = "Lorem 21 ipsum red"

# . ^ * + ? $ {}  []  {} \  |

print("=============== re.search('pattern', str)===============")
print(f"\t{str1:<20}  -----> {re.search('1',str1)}")
print(f"\t{str2:<20}  -----> {re.search('1',str2)}")
print(f"\t{str3:<20}  -----> {re.search('1',str3)}")
print("========================================================")

print("=============== re.search('pattern', str)===============")
print(f"\t{str1:<20}  -----> {re.search('12',str1)}")  # 12
print(f"\t{str2:<20}  -----> {re.search('12',str2)}")  # 12
print(f"\t{str3:<20}  -----> {re.search('12',str3)}")  # 12
print("========================================================")

print("=============== re.search('pattern', str)===============")
print(f"\t{str1:<20}  -----> {re.search('[12]',str1)}") #1 or 2
print(f"\t{str2:<20}  -----> {re.search('[12]',str2)}")  #1 or 2
print(f"\t{str3:<20}  -----> {re.search('[12]',str3)}")  #1 or 2
print("========================================================")


print("=============== re.search('pattern', str)===============")
print(f"\t{str1:<20}  -----> {re.search('[0-9]',str1)}") #1 or 2 or 3 or 5....
print(f"\t{str2:<20}  -----> {re.search('[0-9]',str2)}")  #1 or 2
print(f"\t{str3:<20}  -----> {re.search('[0-9]',str3)}")  #1 or 2
print("========================================================")

print("=============== re.search('pattern', str)===============")
print(f"\t{str1:<20}  -----> {re.search('[a-z]',str1)}") #1 or 2 or 3 or 5....
print(f"\t{str2:<20}  -----> {re.search('[a-z]',str2)}")  #1 or 2
print(f"\t{str3:<20}  -----> {re.search('[a-z]',str3)}")  #1 or 2
print("========================================================")

match = re.search('[a-z]', str1)

if match:
    print("Find any letter")
else:
    print('not found letter')

match = re.search('[a-z]', str3)
if match:
    print("Find any letter")
else:
    print('not found letter')

print("=============== re.search('pattern', str)===============")
print(f"\t{str1:<20}  -----> {re.search('[a-zA-Z]{5}',str1)}") #1 or 2 or 3 or 5....
print(f"\t{str2:<20}  -----> {re.search('[a-zA-Z]{5}',str2)}")  #1 or 2
print(f"\t{str3:<20}  -----> {re.search('[a-zA-Z]{5}',str3)}")  #1 or 2
print("========================================================")

print("=============== re.search('pattern', str)===============")
print(f"\t{str1:<20}  -----> {re.search('[a-zA-Z]+',str1)}") #1 or 2 or 3 or 5....
print(f"\t{str2:<20}  -----> {re.search('[a-zA-Z]+',str2)}")  #1 or 2
print(f"\t{str3:<20}  -----> {re.search('[a-zA-Z]+',str3)}")  #1 or 2
print("========================================================")

print("=============== re.search('pattern', str)===============")
print(f"\t{str1:<20}  -----> {re.search('[a-zA-Z]{3}\W',str1)}") #1 or 2 or 3 or 5....
print(f"\t{str2:<20}  -----> {re.search('[a-zA-Z]{3}\W',str2)}")  #1 or 2
print(f"\t{str3:<20}  -----> {re.search('[a-zA-Z]{3}\W',str3)}")  #1 or 2
print("========================================================")

print("=============== re.search('pattern', str)===============")
print(f"\t{str1:<20}  -----> {re.search('\w+',str1)}")
print(f"\t{str2:<20}  -----> {re.search('\w+',str2)}")
print(f"\t{str3:<20}  -----> {re.search('\w+',str3)}")
print(f"\t{str3:<20}  -----> {re.search('\w+',str3).group(0)}")


print(f"\t{str3:<20}  -----> {re.findall('\w+',str3)}")
print(f"\t{str3:<20}  -----> {re.findall('\w+',str3)[2]}")

match = re.findall('\w+',str3)

for elem in match:
    print(elem, end=" ")
print()
print(f"\t{str3:<20}  -----> {re.sub('\w+', 'summer',str3)}")

#+380961452589
#0961452589
#961452589
#+38096 145 25 89
#+38096-145-25-89
#+38(096)-145-25-89
phoneNumber = input("Enter phone number  ( +380961452589): ")

match = re.search(r'\+\d{2}\(\d{3}\)\-\d{3}\-\d{2}\-\d{2}', phoneNumber)

if match:
    print("Number is correct !!!")
    print(match.group(0))
