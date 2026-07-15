def summaAllNUmber(*args):
    print(args)
    print(args[0])
    #args[0] = 100  -error
    for item in args:
        print(item, end=" ")

    print()
    print(f"Lenght cortege : {len(args)}")
    print(f"Count : {args.count(5)}")
    print(f"Summa : {sum(args)}")
    print(f"Find element 55 : {args.index(55)}")
    print(f"Find element 88 : {args.index(88)}")
    print(f"Count number 88: {args.count(88)}")
    #args[5]=1000
    numbers = list(args)
    print("Numbers : ")
    numbers[0] = 100
    for item in numbers:
        print(item, end=" ")

summaAllNUmber(55,66,77,88, 88, 88, 88)
# summaAllNUmber(5,5,5,5,5)
# summaAllNUmber(5,6)
# summaAllNUmber(5,6,7)
# print()
# print(5)
# print(5,10)
# print(5,10,55)
# print(5,10,55,"Hello")

def printList(name_list, *args):
    print()
    print(name_list)
    for num in args:
        print(num, end=" ")

printList("Standart list",5,7,14,3,2,9,6,8)
printList("Sorted list",1,2,3,4,5,6,7)


#lambda function 
def suma(a,b):
    return a+b

def show(color):
    print(color)

print(suma(3,7))
show("red")
show("green")
print(show)
print(suma)

lambda_show = lambda color:print(color)
lambda_show("red")


#lambda_sum = suma# suma 0x000002A9C88733D0 --> lambda_sum 0x000002A9C88733D0
lambda_sum = lambda a,b:a+b
print(lambda_sum)
print(suma)
print(lambda_sum(3,3))
print(suma(3,3))

import random 
numbers = [random.randint(1,10)  for i in range(20)]
for i in numbers:
    print(i , end=" ")

def changeNumbers(list):
    temp = []
    for i in numbers:
        temp.append(i*2)
    return temp

numbers = changeNumbers(numbers)
print()
for i in numbers:
    print(i , end=" ")

# def double(a):
#     return a*2
print("\n-------------------------------")
print(numbers)
#new_numbers = list(map(double, numbers))
new_numbers = list(map(lambda a:a*2, numbers))
print(new_numbers)
new_numbers = list(map(lambda a:a**2, numbers))
print(new_numbers)

# line = input("\nEnter all numbers").split(' ')
# line= [int(item) for item in line]
# print(line)
# line = list(map(int, input("\nEnter all numbers").split(' ')))
# print(line)
numbers = [random.randint(1,20)  for i in range(20)]
print(numbers)
even_numbers= list(filter(lambda a : a%2 == 0, numbers))
print(even_numbers)

filter_numbers= list(filter(lambda a : a>0 and a < 6, numbers))
print(filter_numbers)
colors = ['red','green','blue','yellow','pink','black', 'grey']
four_color = list(filter(lambda color:len(color)== 4, colors))
print(four_color)
four_color = list(filter(lambda color:color[0]== 'b', colors))
print(four_color)


#1 рядок
print(f'{chr(9556)}{chr(9552)*5}{chr(9574)}{chr(9552)*8}{chr(9574)}{chr(9552)*25}{chr(9574)}{chr(9552)*10}{chr(9574)}{chr(9552)*10}{chr(9559)}')

#2 рядок
print(f'{chr(9553)}{'No':^5}{chr(9553)}{'Item':^8}{chr(9553)}{'Description':^25}{chr(9553)}{'Quality':^10}{chr(9553)}{'Price':^10}{chr(9553)}')

#3 рядок
print(f'{chr(9568)}{chr(9552)*5}{chr(9580)}{chr(9552)*8}{chr(9580)}{chr(9552)*25}{chr(9580)}{chr(9552)*10}{chr(9580)}{chr(9552)*10}{chr(9571)}')

#4 рядок
print(f'{chr(9553)}{'1':^5}{chr(9553)}{'P196':^8}{chr(9553)}{'Samsung Color TV':^25}{chr(9553)}{'1':^10}{chr(9553)}{'$ 829.00':^10}{chr(9553)}')

#5 рядок
print(f'{chr(9553)}{'2':^5}{chr(9553)}{'P020':^8}{chr(9553)}{'Uniden Handset':^25}{chr(9553)}{'1':^10}{chr(9553)}{'$ 29.00':^10}{chr(9553)}')

#6 рядок
print(f'{chr(9553)}{'3':^5}{chr(9553)}{'P111':^8}{chr(9553)}{'Folder Blank':^25}{chr(9553)}{'1':^10}{chr(9553)}{'$ 2.70':^10}{chr(9553)}')

#7-9 рядок
print(5*(f'{chr(9553)}{(' ')*5}{chr(9553)}{(' ')*8}{chr(9553)}{(' ')*25}{chr(9553)}{(' ')*10}{chr(9553)}{(' ')*10}{chr(9553)}\n'),end='')


#10 рядок
print(f'{chr(9568)}{chr(9552)*5}{chr(9580)}{chr(9552)*8}{chr(9580)}{chr(9552)*25}{chr(9580)}{chr(9552)*10}{chr(9580)}{chr(9552)*10}{chr(9571)}')

#11 рядок
print(f'{chr(9553)}{(' ')*5}{chr(9553)}{(' ')*8}{chr(9553)}{(' ')*25}{chr(9553)}{(' ')*10}{chr(9553)}{(' ')*10}{chr(9553)}')

#11 рядок
print(f'{chr(9562)}{chr(9552)*5}{chr(9577)}{chr(9552)*8}{chr(9577)}{chr(9552)*25}{chr(9577)}{chr(9552)*10}{chr(9577)}{chr(9552)*10}{chr(9565)}')


input("Enter numner")