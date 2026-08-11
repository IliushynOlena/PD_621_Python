
# #try  except
# num1 = None
# num2 = None
# a = 5
# b = 0
# while num1 == None or num2 == None:
#     try:
#         num1 = int(input("Enter number : "))
#         num2 = int(input("Enter number : "))
#         print(f"Number : {num1}")
#         print(f"Number : {num1/num2* num3}")
#         #print(f"Number : {num1/num2*num3}")
#     except ValueError :
#         print("Error value enter. Enter number")
#     except ZeroDivisionError:
#         print("Don't divide by zero!!! Study math!!!")
#     except Exception:
#         print("Some Error")

# print("Continue......")
# print("End!!!")

# numbers = list((1,2,3,5))

# print("Hello")
# try:
#     age = int(input("Enter age : "))
  
#     if age < 0 :
        
#         raise Exception("Age error. Age < 0")
#     elif age > 120:
#         raise Exception ("Age error. Age > 120")          
#     else:
#         print(f"Your age = {age}")
     
# except ValueError:
#     print("Value error. Enter age (number)")
# except Exception as ex:
#     print(ex) 
# else:
#     print("Good job!!!")
# finally:
#     #close all files
#     #close connection to database
#     print("Finally")
#     print("Work always")


# print("Continue......")

colors = ['red', 'green','yellow','white','grey']

def showElement(index):
    print(f"Element in index [{index}] - {colors[index]}")

def showElementWithEx(index):
    #index - correct ????
    try:
        if index >= 0 and len(colors)-1:
            print(f"Element in index [{index}] - {colors[index]}")  
        else:
            raise IndexError("Your index is incorrect")  
    except IndexError as ex:
        print(ex)

showElementWithEx(4)
try:
    index = int(input("Enter index element : "))
    showElement(index)
except ValueError as v:
    print(v)
    print("Enter index (number)")
except IndexError:
    print("Index out of range")
except Exception as ex:
    print(ex)