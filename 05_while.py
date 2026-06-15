
i = 0 # 1 - create counter 
while i < 10: # 2 - use counter in condition
    print(i ,"Hello world")
    i+= 1

# 5 -  20
i = 5
while i <= 20:
    print(i,end='  ')
    i+=1

print("Continue....")

#вивести всі числа від 10 до 0
print("вивести всі числа від 10 до 0")
i = 10 #лічильник
while i >= 0: # використати лічильник в умові
    print(i, end=" ")  
    i-=1 # збільшуємо / зменшуємо лічильник


print('''\nкористувач вводить число… 
вивести  всі числа від 
введеного користувачем значення до 20
''')
number = int(input("Enter number : "))

if number <= 20:
    while number <= 20:
        print(number, end=" ")
        number += 1
else:
    ##number = 28......20
    while number >= 20:
        print(number, end=" ")
        number -=1

#користувач вводить число…вивести таблицю множення на це число
number = int(input("\nEnter number : "))

if number < 0 or number > 10:
    print("Error number ")
else:
    i = 1
    while i <= 10:
        print(f"{number} * {i} = {number*i}")
        i += 1
    else:
        print("="*30)
