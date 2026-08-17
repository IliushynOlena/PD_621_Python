import json

login = "user1"
password = "123456"
email = "user1@gmal.com"
score = 0
hp = 100


login1 = "user1"
password1 = "123456"
email1 = "user1@gmal.com"
score1 = 0
hp1 = 100

user1 = [ "user1","123456", "user1@gmal.com", 0, 100]
user2 = [ "user1","123456", "user1@gmal.com", 0, 100]
user3 = [ "user1","123456", "user1@gmal.com", 0, 100]
user4 = [ "user1","123456", "user1@gmal.com", 0, 100]

# dictionary {} -->  key:value

student = {
    #key(only str): value (any type)
    'name':'Oleg',
    'surname':'Ivanchuk',
    'age':17,
    'study place': "IT Step",
    'rating' : 11.8,
    'group': 'PD621',
    'course':'programming',
    'birthdate':'01.06.2009'
}
print(student)
print(student["name"])
print(student['surname'])
print(student['study place'])
print(f"Fullname : {student["name"]} {student["surname"]}.\nGroup {student['group']}. RAting {student['rating']}")

for key in student.keys():
    print(f"{key} - {student[key]}")

print()

for value in student.values():
    print(f"\t{value}")

print()
for key, value in student.items():
    print(f"{key} - {value}")

print(student.keys())
print(student.values())
print(student.items())

print(student)
del student['birthdate']
print(student)
student.popitem()
print(student)
student.pop('age')
print(student)

student['email'] = 'superpuperuser@gmail.com'
student['emaile'] = 'superpuperuser@gmail.com'
student['homeaddress'] = 'Rivne, Soborna 285'
print(student)


students_list = [
    {'name1':"Stas",'surname':"Ivanchuk",'rating':11.5, 'birthdate':"01.06.2009"},
    {'name1':"Olga",'surname':"Popchuk",'rating':7.5, 'birthdate':"01.12.2009", "marks":[7,6,5,8,10,11]},
    {'name1':"Mukola",'surname':"Oliunuk",'rating':9.8, 'birthdate':"01.10.2009"},
    {'name1':"Ira",'surname':"Petruk",'rating':11.0, 'birthdate':"01.04.2009"}
]
print(students_list)
print(students_list[1]["name1"])
print(students_list[1]["rating"])
print(students_list[1]["marks"])
print(students_list[1]["marks"][0])

print("MArks Olga : ")
for m in students_list[1]["marks"]:
    print(m, end= " ")
print()

print(student)
# name_key = input("Enter key to change value : ")
# for item in students_list:
#     print(item.keys())
#     if name_key in item.keys():
#         print(f"{name_key} is in dictionary ")
#     else:
#         print("key not found")
student = {
    #key(only str): value (any type)
    'name':'Oleg',
    'surname':'Ivanchuk',
    'age':17,
    'study place': "IT Step",
    'rating' : 11.8,
    'group': 'PD621',
    'course':'programming',
    'birthdate':'01.06.2009'
}
with open("student_save.json",'w') as file:
    student_serialize = json.dumps(student)
    file.write(student_serialize)

print("Read student from file")
with open("student_save.json",'r') as file:
    info = file.read()
    #print(file.read()['name'])
    new_student = json.loads(info)
    print(new_student)





# print(type(student))
# print(student)

# student_serialize = json.dumps(student)
# print(type(student_serialize))
# print(student_serialize)

# new_student = json.loads(student_serialize)
# print(type(new_student))
# print(new_student['name'])

print(students_list)



def addNewStudent(student, students_list):
    students_list.append(student)



new_student = {
    #key(only str): value (any type)
    'name':'name1',
    'surname':'surname1',
    'age':1,
    'study place': "study",
    'rating' : 11.8,
    'group': 'PD621',
    'course':'programming',
    'birthdate':'01.06.2009'
}
addNewStudent(new_student, students_list)
print(students_list)


print("\t\t\t MEnu\n\t\t1 - Add new  .\n\t\t2 - Remove\n\t\t3 - Change students")
choice = int(input("Enter your choice : "))
if choice == 1:
    addNewStudent(new_student, students_list)
    print(students_list)
