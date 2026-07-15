def modifyName(userName):
    newName1 = userName.upper()
    newName2 = userName.lower()

    return newName1, newName2
   


# name = input("Enter name  : ")
# print(modifyName(name))
# user_name_1, user_name_2 = modifyName(name)
# print(user_name_1)
# print(user_name_2)

a,b,c = 1, 2,3
print(a,b,c)

def checkLog(userLog):
    if userLog == 'admin':
        return userLog.upper()
    elif userLog =='user':
        return userLog.lower()
    else:
        return "Wrong login!"
    
print(checkLog('admin'))
print(checkLog('user'))
print(checkLog('student'))

'''
def name_function(*args):
    some code

name_function(1,2,3,4,5,6)
'''
import random
def myFunction(*args):
    s = 0
    k = 0
    print(args)
    for i in args:
        s += i
        k +=1
    return s/k

print(myFunction(1,2,3))
print(myFunction(1,2,3,4,5,6))
print(myFunction(1,2,3,4,5,6,45,62,8))

numbers = [random.randint(1,15)  for i in range(20)]
print(numbers)
print(myFunction(*numbers))


#Recursion

def printHello():
    print("hello")
    printHello()



# print(printHello) 
# printHello()

#5 ! = 1*2*3*4*5  = 120
def factorial(number):
    if number == 1:
        return 1
    return number * factorial(number-1)
#return 5 * 4 * 3 * 2 * 1

print(factorial(5))

def isStrPalindrome(myStr):
    if myStr == myStr[::-1]:
        print('palindrome')
    else:
        print('not palindrome')
isStrPalindrome("madam")
isStrPalindrome("hello")

def isPalindrome(myStr):
    if len(myStr) == 0:
        return True
    else:
    #d
        if myStr[0] == myStr[-1]:
            return isPalindrome(myStr[1:-1])
        else:
            return False
userStr = input("Enter text : ")
if isPalindrome(userStr.lower())  == True:
    print("Palindrome")
else:
    print("Not palindrome")