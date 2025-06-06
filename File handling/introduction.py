#Open Function has two parameters open("File name with location" , "mode of opening")
file = open("intro.txt" , "r")

#This function will read content from the file by looping whole file
content = file.read()
print(content)
print("")
file.close()

#This Function will also read the content line by line fom the file
file1 = open("intro.txt")
line_list = file1.readlines()
print(type(line_list))
for line in file1.readlines():
    print(line, end="")
file1.close()

#Append or Write text into the file 
file2 = open("intro.txt" , "a")
file2.write("\nThis Text is appended by the python program.....")
file2.close()