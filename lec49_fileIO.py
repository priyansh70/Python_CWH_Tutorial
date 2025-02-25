# Python provides several ways to manipulate file.

# Opening File 
f = open('myfile.txt','r') #r = read mode
# r = Read mode [Default Mode]
# w = write mode [Write Only] [Create new file, if not exists] [Already Written text override]
# a = append mode [Append Only] [Create new file, if not exists]
# x = create mode [Create File] [Give Error, if file already exists]
# t = text mode
# b = binary mode

# Read Content of the File 
print(f.read())

# Close the file 
f.close()

# WRITE FILE 
f = open("myfile.txt",'w')
f.write("This file is used for Lecture 49")

# Close the file 
f.close()

# APPEND FILE 
f = open("myfile.txt",'a')
f.write(". It is very Nice Content")

# Close the file 
f.close()

# f = open("myfile.txt",'x') 

# We can avoid close by using with keyword 
with open("myfile2.txt",'a') as f:
    f.write("It is a 2nd Text File")