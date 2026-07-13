
# def showMessage():
#     a = 5
#     print("Hello" , a)

# showMessage()
# showMessage()
# showMessage()
# showMessage()

# def showHelloUser(name):
#     print(f"Hello {name}")

# showHelloUser("Denus")
# showHelloUser("Iruna")
# showHelloUser("Anna")

# # name = input("Enter name : ")
# # showHelloUser(name)


# # def summa(a,b):
# #     print(a + b)

# def summa(a,b):
#     # res = a + b
#     # return res
#     return a + b

# def sub(a,b):
#     return a-b 

# def multy(a,b):
#     return a*b 

# def div(a,b):
#     if b == 0:
#         return#break
#     return a/b 

# def calculator(a,b,op):
#     if op == '+':
#         return summa(a,b)
#     if op == '-':
#         return sub(a,b)
#     if op == '*':
#         return multy(a,b)
#     if op == '/':
#         return div(a,b)
    
# def getOperation(line):
#     if line.find('+') != -1:
#         return '+'
#     if line.find('-') != -1:
#         return '-'
#     if line.find('*') != -1:
#         return '*'
#     if line.find('/') != -1:
#         return '/'



# expresion = input("Enter expesion : (5+6) (7-9)")
# operation = getOperation(expresion)
# print(expresion.split(operation))
# num1 = float( expresion.split(operation)[0])
# num2 = float(expresion.split(operation)[1])

# result = calculator(num1,num2,operation)
# print(f"Result = {result}")

# # result = calculator(5,6,'+')
# # print(f"Result = {result}")

# # result = calculator(5,6,'-')
# # print(f"Result = {result}")

# # result = calculator(5,6,'*')
# # print(f"Result = {result}")

# # result = calculator(5,6,'/')
# # print(f"Result = {result}")

# # result = summa(5,5)
# # print(result)
# # print(sub(5,2))
# # s = sub(result, 3)
# # print(s)
# # result = summa(5,9)
# # print(f"Result = {result}")
# # result = summa(15,99)
# # print(f"Result = {result}")
# # result = summa(51,4)
# # print(f"Result = {result}")
# count_elements = 5
# for i in range(count_elements):
#     print(i)

import random
def fillList(new_list,some_number, count_elements = 5, min = 1, max = 10 ):
    new_list = [random.randint(min, max+1)   for i in range(count_elements)]
    return new_list


numbers = []
print(numbers)
numbers = fillList(numbers,10)
print(numbers)

numbers = fillList(numbers)
print(numbers)