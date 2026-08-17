# # name.txt
# # name.html
# # name.py
# # name.cpp
# # name.cs
# # name.png
# # name.css
# # name.exe
# # name.js

# # open file
# # read file
# # write file
# # close file

# url = r'C:\Users\helen\Desktop\PD_621_Python\my_file.txt'
# #file = open('my_file.txt')
# # file = open(url)

# # #print(file.read())
# # #print(file.readline().strip())
# # #print(file.readlines())
# # print(file.read(10))
# # file.close()
# with open(url) as file:
#     print(file.read())
#     #file.close()

# with open('write_file_rewrite.txt', 'w') as file:
#     file.write("Hello world\n")

# with open('write_file_append.txt', 'a') as file:
#     file.write("Hello world\n")

# lines = [
#     'Lorem Ipsum is simply dummy text of the printing and typesetting industry.',
#     'Lorem Ipsum has been the industrys standard dummy text ever since 1966, ',
#     'when designers at Letraset and James Mosley, the librarian at St Bride ',
#     'Printing Library in London, took a 1914 Cicero translation and scrambled '
# ]
# url_2 = "./write_lines.txt"
# # counter = 1
# # with open(url_2, 'w' ) as file:
# #     #file.write(lines) error
# #     for line in lines:
# #         file.write(f"Line number [{counter}] : {line}\n")
# #         counter+=1

# with open(url_2, 'w' ) as file:
#     file.writelines(lines)



# def readFile(filename):
#     with open(filename, 'r' ) as file:
#         #return file.read()
#         return file.readlines()

# def appFileToEnd(filename, info):
#     with open(filename,'a') as file:
#         file.write(info)

# def appFileToEndList(filename, info_list):
#     with open(filename,'a') as file:
#         for line in info_list[::-1]:
#             file.write(f"{line.strip()}\n")
# url_write = "file_write_func.txt"
# url_read = "file_write_func.txt"

# text= readFile('my_file.txt')
# print(text)
# print(text[::-1])

# #appFileToEnd(url_write, text)
# appFileToEndList(url_write, text)


# def testModeFile(filename):
#     with open(filename, 'a+') as file:
#         print(file.readable())
#         print(file.writable())

# testModeFile('my_file.txt')

# with open("write_numbers.txt",'w') as file:
#     file.write(str(55))

# print('a')
# print(chr(65))
# print(chr(65+1))
# print(chr(65+2))


#Напишіть програму, яка копіює вміст файлу 
# data.txt у новий файл backup.txt.
# with open('data.txt','w') as file:
#     file.write("Hello world!\nHello world!\nHello world!")

# def readFile(filename):
#     with open(filename, 'r') as file:
#         return file.read()


# def copyFile(filename, text):
#     with open(filename, 'w') as file:
#         file.write(text)
# copyText = readFile('data.txt')
# copyFile('backup.txt',copyText)


with open('test.txt', 'w+') as file:
    file.write("lzxflkjkdls")
    print(file.readline())