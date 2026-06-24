# number = int(input("Enter number : "))

# i = 1
# while i < 11:
#     print(f"{number} * {i} = {number*i}")
#     i+=1
# print("==============================================")

# for i in range(1,11):
#     print(f"{number} * {i} = {number*i}")

# print("==============================================")
# for i in range(1,11):
#     for j in range(1,11):
#         print(f"{i} * {j} = {i*j}")
#     print()

# print("Continuee.....")

# for i in range(1,6):
#     for j in range(1,6):
#         print('* ',end='')
#     print()

# energy = 70
# floor = 0
# print(f"I am on the {floor} floor")

# while floor != 7:
#     floor+=1
#     print(f"I am on the {floor} floor-------------------")

#     if floor == 3:
#         print("I will take an elevator")
#         break
    
#     stairs  = 0
#     while stairs != 20:
#         print(f"I am on the {stairs} stairs")
#         stairs += 1
#         energy -= 1
#         if energy == 0:
#             print("I am tired! I will rest a little!")
#             energy+=70
#     print("==========================")


   
# print("I am okey. I have got to right floor")


for i in range(1,11):
    for j in range(1,11):
        print('* ',end='')
    print()

print("Головна діагональ")
for i in range(1,11):
    for j in range(1,11):
        if i == j:
            print('* ',end='')
        else:
            print('= ',end='')
    print()

print("Побічна діагональ")
N = 11
for i in range(0,N):
    for j in range(0,N):
        if i + j == N - 1:
            print('- ',end='')
        else:
            print('+ ',end='')
    print()

for num in range(2,10):    
    flag = True
    for i in range(2,num//2+1):#1....5
        if num%i == 0:
            flag = False
            break

    if not flag:
        print("composite", num)
    else:
        print("Simple", num)
    


