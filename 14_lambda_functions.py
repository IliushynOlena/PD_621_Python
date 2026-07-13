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