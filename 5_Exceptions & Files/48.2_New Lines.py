import os
names = ["John", "Oscar", "Jacob"]

file = open("names.txt", "w+")
#write down the names into the file
for i in range(len(names)):
    file.write(names[i])
    file.write("\n")
file.close()
file= open("names.txt", "r")
#output the content of file in console
print(file.read())

file.close()