matrix = [
    [1,2,3,4,7],
    [5,6,7,8,7],
    [9,10,11,12,77],
    [9,10,11,12,77],
]

print(matrix)

for item in matrix:
    print(item)

print(f"Lenght matrix {len(matrix)}")
print(matrix[0])
print(len(matrix[0]))
for i in range(len(matrix)):# 0  1  2
    for j in range(len(matrix[i])):
        print(f"{matrix[i][j]:>3}", end=" ")
    print()
    
import random
matrix= []
row = 5
col = 6
for i in range(row):
    numbers = []
    for j in range(col):
        numbers.append(random.randint(10,100))
    matrix.append(numbers)
for i in range(row):# 0  1  2
    for j in range(col):
        print(f"{matrix[i][j]:>3}", end=" ")
    print()
