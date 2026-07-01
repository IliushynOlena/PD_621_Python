
myStr = 'football'
print(myStr[0])
print(myStr[7])
print(myStr[len(myStr)-1])#lenth = 8   index = 7
print(myStr[-1])


line = "Hello world. It is very hot today!"

print(line[0])
print(line[0:5])
print(line[:8]) # start  = 0, end = 8
print(line[5:]) # start  = 5, end = len(line)-1
print(line[-5:-2]) # start  = 5, end = len(line)-1
print(line[:-1]) # start  = 5, end = len(line)-1
print(line[:]) # start  = 0, end = len(line)-1

print(line[2:10:2]) 
print(line[10:2:-2]) 
print(line[::-1]) 

#methods str()

numbers = '123456789'
letters = 'asslfkjsdkds'
line = "Lorem ipsum dolor sit emet"
word = "Fruit Apple"
word2 = "BANANA"
leterDigit = "ffs2sf1s54f5f"

print("\n\t===================== isalnum()=============")# тільки букви і цифри
print(f"\t{numbers:<30}----------> {numbers.isalnum()}")
print(f"\t{letters:<30}----------> {letters.isalnum()}")
print(f"\t{line:<30}----------> {line.isalnum()}")
print(f"\t{word:<30}----------> {word.isalnum()}")
print(f"\t{word2:<30}----------> {word2.isalnum()}")
print(f"\t{leterDigit:<30}----------> {leterDigit.isalnum()}")

print("\n\t===================== isalpha()=============")# тільки букви 
print(f"\t{numbers:<30}----------> {numbers.isalpha()}")
print(f"\t{letters:<30}----------> {letters.isalpha()}")
print(f"\t{line:<30}----------> {line.isalpha()}")
print(f"\t{word:<30}----------> {word.isalpha()}")
print(f"\t{word2:<30}----------> {word2.isalpha()}")
print(f"\t{leterDigit:<30}----------> {leterDigit.isalpha()}")

print("\n\t===================== isdigit()=============")# тільки цифри 
print(f"\t{numbers:<30}----------> {numbers.isdigit()}")
print(f"\t{letters:<30}----------> {letters.isdigit()}")
print(f"\t{line:<30}----------> {line.isdigit()}")
print(f"\t{word:<30}----------> {word.isdigit()}")
print(f"\t{word2:<30}----------> {word2.isdigit()}")
print(f"\t{leterDigit:<30}----------> {leterDigit.isdigit()}")


print("\n\t===================== isspace()=============")# тільки пробіли 
print(f"\t{numbers:<30}----------> {numbers.isspace()}")
print(f"\t{letters:<30}----------> {letters.isspace()}")
print(f"\t{line:<30}----------> {line.isspace()}")
print(f"\t{word:<30}----------> {word.isspace()}")
print(f"\t{word2:<30}----------> {word2.isspace()}")
print(f"\t{leterDigit:<30}----------> {leterDigit.isspace()}")

print("\n\t===================== islower()=============")# тільки маленькі букви 
print(f"\t{numbers:<30}----------> {numbers.islower()}")
print(f"\t{letters:<30}----------> {letters.islower()}")
print(f"\t{line:<30}----------> {line.islower()}")
print(f"\t{word:<30}----------> {word.islower()}")
print(f"\t{word2:<30}----------> {word2.islower()}")
print(f"\t{leterDigit:<30}----------> {leterDigit.islower()}")

print("\n\t===================== isupper()=============")# тільки великі букви 
print(f"\t{numbers:<30}----------> {numbers.isupper()}")
print(f"\t{letters:<30}----------> {letters.isupper()}")
print(f"\t{line:<30}----------> {line.isupper()}")
print(f"\t{word:<30}----------> {word.isupper()}")
print(f"\t{word2:<30}----------> {word2.isupper()}")
print(f"\t{leterDigit:<30}----------> {leterDigit.isupper()}")

print("\n\t===================== istitle()=============")# перевіряє рядок - кожна перша буква велика 
print(f"\t{numbers:<30}----------> {numbers.istitle()}")
print(f"\t{letters:<30}----------> {letters.istitle()}")
print(f"\t{line:<30}----------> {line.istitle()}")
print(f"\t{word:<30}----------> {word.istitle()}")
print(f"\t{word2:<30}----------> {word2.istitle()}")
print(f"\t{leterDigit:<30}----------> {leterDigit.istitle()}")

print("\n\t===================== lower()=============")# перетворює всі букви на малі
print(f"\t{numbers:<30}----------> {numbers.lower()}")
print(f"\t{letters:<30}----------> {letters.lower()}")
print(f"\t{line:<30}----------> {line.lower()}")
print(f"\t{word:<30}----------> {word.lower()}")
print(f"\t{word2:<30}----------> {word2.lower()}")
print(f"\t{leterDigit:<30}----------> {leterDigit.lower()}")

print("\n\t===================== upper()=============")# перетворює всі букви на великі
print(f"\t{numbers:<30}----------> {numbers.upper()}")
print(f"\t{letters:<30}----------> {letters.upper()}")
print(f"\t{line:<30}----------> {line.upper()}")
print(f"\t{word:<30}----------> {word.upper()}")
print(f"\t{word2:<30}----------> {word2.upper()}")
print(f"\t{leterDigit:<30}----------> {leterDigit.upper()}")

print("\n\t===================== capitalize()=============")# перетворює першу букви на велику
print(f"\t{numbers:<30}----------> {numbers.capitalize()}")
print(f"\t{letters:<30}----------> {letters.capitalize()}")
print(f"\t{line:<30}----------> {line.capitalize()}")
print(f"\t{word:<30}----------> {word.capitalize()}")
print(f"\t{word2:<30}----------> {word2.capitalize()}")
print(f"\t{leterDigit:<30}----------> {leterDigit.capitalize()}")

print("\n\t===================== title()=============")# перетворює першу букву кожного слова на велику
print(f"\t{numbers:<30}----------> {numbers.title()}")
print(f"\t{letters:<30}----------> {letters.title()}")
print(f"\t{line:<30}----------> {line.title()}")
print(f"\t{word:<30}----------> {word.title()}")
print(f"\t{word2:<30}----------> {word2.title()}")
print(f"\t{leterDigit:<30}----------> {leterDigit.title()}")

print("\n\t===================== swapcase()=============")# міняємо регістри
print(f"\t{numbers:<30}----------> {numbers.swapcase()}")
print(f"\t{letters:<30}----------> {letters.swapcase()}")
print(f"\t{line:<30}----------> {line.swapcase()}")
print(f"\t{word:<30}----------> {word.swapcase()}")
print(f"\t{word2:<30}----------> {word2.swapcase()}")
print(f"\t{leterDigit:<30}----------> {leterDigit.swapcase()}")

#Find()
line = "Lorem ipsum dolor sit emet ipsum dolor sit ipsum dolor sit ipsum dolor sit ipsum dolor sit"
print(f"\t{line:<30}----------> index [ipsum] -- {line.find("ipsum")}")#------------>
print(f"\t{line:<30}----------> index [ipsum] -- {line.find("ipsum",7)}")
print(f"\t{line:<30}----------> index [ipsum] -- {line.find("ipsum",28)}")
print(f"\t{line:<30}----------> index [ipsum] -- {line.find("ipsum",44)}")
print(f"\t{line:<30}----------> index [ipsum] -- {line.find("ipsum",60)}")
print(f"\t{line:<30}----------> index [ipsum] -- {line.find("ipsum",76)}")

index = -1
while True:
    index = line.find("sit", index+1)
    if index == -1:
        print("Word not found")
        break
    print(f"Index = [{index}] found word = sit")


print(f"\t{line:<30}----------> index [ipsum] -- {line.rfind("ipsum")}")#<----------
print(f"\t{line:<30}----------> index [ipsum] -- {line.index("ipsum")}")#----->
print(f"\t{line:<30}----------> index [ipsum] -- {line.index("ipsum",7)}")#----->
#print(f"\t{line:<30}----------> index [ipsum] -- {line.index("hello")}")#----->
print(f"\t{line:<30}----------> index [ipsum] -- {line.rindex("ipsum")}")#<----------


print(f"\t{line:<30}----------> index [ipsum] -- {line.count("ipsum")}")#<----------
print(f"\t{line:<30}----------> index [ipsum] -- {line.count("SIT")}")#
print(f"\t{line:<30}----------> index [ipsum] -- {line.count("sit")}")#

print(f"\t{line:<30}----------> index [ipsum] -- {line.replace("sit", 'SIT')}")#


print(f"\t{line:<30}----------> index [ipsum] -- {line.endswith('sit')}")#
print(f"\t{line:<30}----------> index [ipsum] -- {line.endswith('hello')}")#

print(f"\t{line:<30}----------> index [ipsum] -- {line.startswith('sit')}")#
print(f"\t{line:<30}----------> index [ipsum] -- {line.startswith('hello')}")#

myStr = "I love Python"
print(f"=={myStr:^30}==")

print(myStr.center(30))
print(myStr.center(30,'*'))
print(myStr.center(30,'='))
print(myStr.center(5))
print(myStr.rjust(30))
print(myStr.ljust(30,'@'))
print(myStr.rjust(30,'-'))

email = "                superpuperemail@gmail.com      "
print(f"={email}=")
print(f"={email.lstrip()}=")
print(f"={email.rstrip()}=")
print(f"={email.strip()}=")


line = 'lflkf64465'

print(line[0])
print(line[1])
print(line[2])

for letter in line:
    print(letter)
    letter.isalpha()

