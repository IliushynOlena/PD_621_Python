# a = 7
# b = 8
# c = 4
# pi = 3.14

# # - однорядковий коментар
# #   print(a,b,c, pi)
# ''' Багаторядковий коментар
# print(a,b,c, pi)
# print("Numbers : ", "a =", a, "b =", b, "c =",c, "pi = ", pi)
# print("Numbers : a = {}, b = {}, c = {}, pi = {}".format(a,b,c, pi))
# print("Numbers : a = {}, b = {}, c = {}, pi = {}".format(a, pi, c, b))
# print(f"Numbers : a = {a}, b = {b}, c = {c}, pi = {pi}")
# '''
# # Ctr + K + C - comment selected code
# # Ctr + K + U - uncomment selected code
# # print("Hello world")
# # print("Hello world")
# # print("Hello world")
# print("Hello world")
# print("Hello world")
# if True:
#     print("Hello world")

# print("Hello world")
# print('Hello world')

# a = "Happy "
# b = "New Year"
# print(a+b)

# a = "Happy New Year "
# b = 2026
# #print(a+b)

# # x = 5
# # print(x+y)
# # y = 
# x = 5
# y = 7
# x = y#<------- = оператор присвоєння
# print(x == y)# == оператор порівняння

# import math
# print(math.ceil(2.5)) # 2.5 ---> 3  заокруглює до більшого
# print(math.floor(2.5)) # 2.5 ---> 2 заокруглює до меншого
# print(math.pow(2,4)) # 2*2*2*2 підносить до степеня
# print(math.sqrt(16)) # sqrt(16) = 4  корінь квадратний


# import random
# print(random.random()) #0......1
# print(random.randint(0,1)) #0 or 1
# print(random.randint(100,200)) #100 or 200
# print(random.randint(10,20)) #10 or 20

# price_1 = 270
# price_2 = 200

# weight_candy_in_gram = int(input("Enter weight (gram)"))
# kg = weight_candy_in_gram/1000
# print(f"Your weight :  {kg} kg")
# if kg < 0.5:
#     total_price = kg * price_1
# else:
#     total_price = kg * price_2

# print(f"You need to pay : {math.ceil(total_price)} grn")


day = int(input("Enter number day [1-7] --> "))
if day == 1 :
    print("Monday")
elif day == 2 :
    print("Tuesday")
elif day == 3 :
    print("Wednesday")
else:
    print("Error number day")


num = 8
num % 2 == 0




day = int(input("Enter number day [1-7] --> "))
match day:
    case 1:
        print("Monday")
    case 2:
        print("Tuesday")
    case 3:
        print("Wednesday")
    case _:
        print("Error number day")


