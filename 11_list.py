
marks = []#empty list
category = ["Drama","Comedy", "Fantasy"]

courses = list(("Math","Databases","Physic"))

print(category)
print(courses)
print(category[0])
print(courses[0])

count_negative = 0
max= category[0]
for one_item in category:
    print(one_item)
    if one_item  < 0:
        count_negative+=1

for one_item in courses:
    print(one_item)

studentScores = []
students = list()
print(studentScores)
print(students)


myCourse = ["Math", 2345, 7009, "Physic",True, 3.14]
print(myCourse)

customers = ["Bob", "Anna","Inna","Bob","Jack","Anna"]
print(customers)

mySymbols = list('asddfgh')
print(mySymbols)
word = list(("Hello", "green"))
print(word)

#newList = [expression for i in sequence]
#for i in range(10) : 0 1 2 3 4 5 6 7 8 9 
list1 = [i for i in range(10)]
print(list1)

list1 = [i*i for i in range(10)]
print(list1)

import random
numbers = [random.randint(10,50)       for i in range(10)]
print(numbers)
print(f"Length numbers : {len(numbers)}")


#for i in"example"  e x a m p l e
list2 = [i+'*'      for i in"example"]
print(list2)

for s in "language":
    print(s, end="-")

line = [s for s in "language"]
print(line)
print(line[0])
print(line[1])
print(" - ".join(line))

line = "blue red green yellow pink black grey white orange brown"
print(f"Length colors : {len(line)}")
list_colors = line.split(" ")
print(list_colors)
print(f"Length colors : {len(list_colors)}")

#newList = [expression for i in sequence  if condition]
#for i in range(20): --> 0  2  4  6  8  ...19
list4 = [i*i for i in range(20) if i%2 == 0]
print(list4)

customers = ["Bob", "Anna","Inna","Bob","Jack","Anna"]
list5 = [c for c in customers if c!="Bob" and c != "Inna"]
print(list5)


#for x in range(1,4) --> x --> 1 2 3
#for y in range(1,4) -> y = 1 2 3
for x in range(1,4):#x = 1   x = 2  x = 3
    for y in range(1,4):# 1*1 1*2  1*3   2*1  2*2  2*3   3*1  3*2  3*3
        print(x*y)
    print()
list6 = [x*y for x in range(1,4) for y in range(1,4)]
print(list6)

myList = ["user", 12, 220.34, False,True]
print(myList[0])
print(myList[-1])
print(myList[len(myList)-1])

print(myList[:])
print(myList[1:3])
print(myList[:4])
print(myList[2:])
print(myList[2::2])

category = ["Drama","Comedy", "Fantasy"]
print(category)
category[-1] = "Action"
print(category)

prices = [100,150,245.23,1200,25147,63,4.15]
print(f"Lenght : {len(prices)}")
print(f"Sorted : {sorted(prices)}")
print(f"Max : {max(prices)}")
print(f"Min : {min(prices)}")
print(f"Sum : {sum(prices)}")
category = ["Drama","Comedy", "Fan",  "Forest",  "Forget"]
#print(f"Sum : {sum(category)}")#summa = 0
print(f"MAx : {max(category)}")#summa = 0

category1 = ["Drama","Comedy"]
category2 = ["Fantasy"]
print(category1+ category2)
print(category1*3)

for el in category1:
    print(el)
print("--------------------------------------------")
for i in range(len(category1)):
    print(category1[i])

#methods 
category1.append("Fantasy")#add to the end
print(category1)

category1.extend(["Horor","Mystery"])#add colection to the add
print(category1)

category1.insert(2,"Novel")# add to the position
category1.insert(0,"Romance")
category1.insert(-1,"Romance")
print(category1)

category1.remove("Romance")#delete by value
print(category1)
category1.pop()#delete from end
print(category1)
category1.pop(2)
print(category1)


#category1.clear()#delete all collection
#print(category1)

print(category1.index('Fantasy'))
#print(category1.index('Fantasyy')) #error

print(category1.count("Drama"))

category1.sort()
print(category1)

category1.sort(reverse=True)
print(category1)



customers = ["Bob", "Anna","Inna","Bob","Jack","Anna"]
print('Bob' in customers)
print('Andriy' in customers)
if 'Bob' in customers:
    print("User Bob is in list customers")

list1 = [1,2,3,4,5]
list2 = list1
print(list1)
print(list2)

list2[0] = 100
print(list1)
print(list2)
print(id(list1))
print(id(list2))

list_copy = list1.copy()
list_copy[0] = 222
print(list1)
print(list_copy)
print(id(list1))
print(id(list_copy))

list_copy2 = list(list1)
list_copy2[0] =22
print(list1)
print(list_copy2)




