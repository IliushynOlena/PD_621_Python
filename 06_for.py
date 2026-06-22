line = "Hyper text markup language tr"

print(line)
print(len(line))
print(f"Lenght : {len(line)}")

print(line[0])
print(line[1])
print(line[2])

i = 0
lenght = len(line)
while i < lenght:
    print(line[i], end=" ")
    i+=1

print()

for s in line:
    print(s, end=" ")

print()
print(line)

print()
# line[start:end] # start = 0  end = 26
for s in line[:]:
    print(s, end=" ")

print()
# line[start:end]   start = 5   end = 26
for s in line[5:]:
    print(s, end=" ")

print()
## line[start:end]   start = 0 end = 5
for s in line[:5]:
    print(s, end=" ")

print()
## line[start:end]   start = 6 end = 10
for s in line[6:10]:
    print(s, end=" ")

print()
## line[start:end:step]   start = 0 end = 5  step = 1
for s in line[::]:
    print(s, end=" ")

print()
## line[start:end:step]   start = 0 end = 5  step = 2
for s in line[0:len(line):2]:
    print(s, end=" ")

#1.....10
print()
#range(start,stop, step)
for num in range(1,11):#1......10  num  5
    print(num, end=" ")

print()
for num in range(10,20):#10.....19
    print(num, end=" ")

print()
for num in range(5):#0.....4
    print(num, end=" ")

print()
for num in range(10,20,3):#10 12 14 16 18 
    print(num, end=" ")

# while True:
#     num = int(input(" 2 + 2 = ???   --> "))

#     if num ==4 :
#         print("Success")
#         break

# n = int(input(" Enter number "))

# #continue
# i = 0 #0...n
# while i <= n:
#     i+=1
#     if i%3 == 0:
#         continue

#     print(i, end=' ')

#3/1= 3  3/3 = 1  3/2=1.5
#4/1 = 4  4/4=1.0 4/2 = 2.0 4/3=1.333
# n = int(input(" Enter number "))
# counter = 0

# #5   5/1   5/2  5/3  5/4 5/5
# #12  12/1 12/2  12/3  12/4  12/5  12/6  12/7  12/8 12/9  
# for i in range(1,n+1):#1....5
#     if n%i == 0:
#         counter+=1

# if counter > 2:
#     print("composite")
# else:
#     print("Simple")


n = int(input(" Enter number "))
flag = True
for i in range(2,n//2+1):#1....5
    if n%i == 0:
        flag = False
        break

if not flag:
    print("composite")
else:
    print("Simple")