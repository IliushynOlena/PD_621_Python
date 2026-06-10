line1 = "Hyper"
line2 = "Text"
line3 = "Markup"
line4 = "Language"

all_line = line1 + " ." + line2 + " ." + line3+ " ." + line4
print(all_line)
print(line1, line2, line3, line4, sep=". ")
print("Hello world! Variables : {}, {}, {}, {}".format(line1,line2,line3,line4))
print(f"Hello world! Variables : \033[31m\033[47m\033[3m {line1}\033[0m, \033[32m\033[46m{line2},\033[33m\033[45m{line3},\033[44m\033[34m {line4}\033[0m")
number = 100
print(number)
print(f"Number = {number}")

print(chr(65))
print(ord('A'))
print(chr(9556),chr(9552)*30)
print(f"{chr(9556)}{chr(9552)*30}")

a = 5
b = 6
# True False
print("1 == 1", 1 == 1)#True
print("1 == 2", 1 == 2)#False
print("1 != 2", 1 != 2)#True
print("1 != 1", 1 != 1)#False
print("1 > 1", 1 > 1)#False
print("1 >= 1", 1 >= 1)#True   1 > 1 or 1 = 1
print("1 < 2", 1 < 2)#True   
print("1 <= 4", 1 <= 4)#True   

print(bool(0)) #False
print(bool(0.0)) #False
print(bool("")) #False
print(bool(None)) #False
print(bool("text")) #True
print(bool(" ")) #True
print(bool(1)) #True

# logic and
competent = True
responsible = True
print(competent and responsible) #True

competent = True
responsible = False
print(competent and responsible)#False

competent = False
responsible = True
print(competent and responsible) #False

competent = False
responsible = False
print(competent and responsible)#False


#logic OR
competent = True
responsible = True
print(competent or responsible)#True

competent = True
responsible = False
print(competent or responsible)#True

competent = False
responsible = True
print(competent or responsible)#True

competent = False
responsible = False
print(competent or responsible)#False

# not
competent = True
print(not competent)#False

competent = False
print(not competent)#True

# age = int(input("Enter age : "))
# #if age >=18  and age <= 120:
# if 18 <= age <= 120:
#     print("You are Adult")
# else:
#     print("Error")

# day = int(input("Enter number day : [1-7]"))
# if day == 1:
#     print("Monday")
# elif day == 2:
#     print("Tuesday")
# elif day == 3:
#     print("Wednesday")    
# else:
#     print("Error number day")

login = input("Enter login : ")
if login == "admin":
    password = input("Enter password :")
    if password == "step":
        print("Welcome")
    else:
        print("Error password ")
elif login == "exit":
    print("Goodbye")
else:
    print("Error")

word = input("Enter word  :")
revers_word = word[::-1]
print(word)
print(revers_word)

num = 12345
a = num//10_000
b = num//1000%10
c = num//100%10
d = num//10%10
e = num %10
print(f"{a} {b} {c} {d} {e}")
