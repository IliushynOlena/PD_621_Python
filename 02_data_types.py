print(123*2)#123 - літерал
print("123"*2)
print("c")

#типи даних
#str
#numbers --> float(3.14), int(100)
#bool --> true, false

#Shift+Alt+ arrow up or arrow down - робимо дублікат рядочка
print("int ", type(2))
print("float ", type(3.14))
print("str ", type("3.14"))
print("bool ", type(False))

# + - * /
print(2 + 2)
print(2 - 2)
print(2 * 2)
print(2 / 2)

#оператор - це символ, який робить 
# певну операцію над даними
#+ - * / // % **

# ** - оператор піднесення до степеня
print(2**3)#2*2*2
print(2**3.0)
print(2.0**3)
print(2.0**3.0)

# * - оператор множення
print(5*5)
print(5*5.0)
print(5.0*5)
print(5.*5.)

# / - оператор ділення з остачею
print(6/4)
print(6/4.)
print(6./4)
print(6./4.)

# // - оператор ділення без остачі (ділення націло)
print(6//4)
print(6//4.)
print(6.//4)
print(6.//4.)

# % - ділення по модулю
#15/3 = 5.0
#15//3 = 5
#15%3 = 0 -->  15/3=5  5*3=15 15-15=0

#9/2 = 4.5
#9//2= 4
#9%2 = 1 --> 9/2=4(.5)  4*2=8  9-8=1

#17%5 = 2????   17/5 = 3.4  3*5 = 15  17-15=2

#21/3 = 7.0
#21%3 = 0  --> 21/3=7    7*3 = 21  21-21 = 0
print(5%2)#1
print(7%4)#3
print(15%4)#3

#print(8/0) division by zero
#print(8%0) division by zero
# унарні(1) --> (-) та бінарні(2) --> (+ - * / % //) оператори
print(5 + 2)
print(+5)
print(-5)
print(-5 + 2)

print(2 + 3 * 5)
print((2 + 3) * 5)

print(5 + 2.6)#7.6
#print(5 + "str")#error --> "str""str""str""str""str"
print(5 + True)#True --> 1
print(5 + False)#False --> 0

#МАГІЧНИМИ числами
print(1000000)
print(1_000_000)

print(12)
print(12*3)
print(36-12)

#Змінна - це ділянка пам*яті, яка маю певну 
# назву та може зберігати значення
name = "Bob"
age = 15
Age = 55
_number = 100
ageofman = 14
age_of_man = 47
#age of man = 47#error
AgeOfMan = 33
a1 = 1
a2 = 2
#3a = 3
#def = 7

var = 100
print(var)
#print(Var)
var = 77
print(var)
number = 44

# first_number = 100
# second_number = 222
#input - введення даних з клавіатури 
first_number = float(input("Enter first number : "))
second_number =  float (input("Enter second number : "))
result = first_number + second_number
print("Summa = ", result)
print(result*2)

line1 = "one"
line2 = "two"
line3 = "three"
line4 = "four"

all_line = line1 +" "+ line2 +" "+ line3 +" "+ line4#конкантенація - додавання рядків
print("="*40)
print("All line : " ,all_line)
print("="*40)

