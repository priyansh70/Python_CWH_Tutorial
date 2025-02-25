# It is a built in module that provides function for interacting with the os. It allows you to perform a wide variety of task, such as reading and writing files, interacting with file system, and running system commands.

import os

# Create Folder 
if(not os.path.exists("data")):
    os.mkdir("data")

# Create Multiple Folder 
# for i in range(100):
#     os.mkdir(f"data/Day{i+1}")

# Rename Folder 
# for i in range(100):
#     os.rename(f"data/Day{i+1}",f"data/Tutorial{i+1}")

# Make List of Folder 
# folders = os.listdir("data")
# print(folders)
# for folder in folders:
#     print(f"{folder} :: {os.listdir(f'data/{folder}')}")


# Delete 
# import stat
# for i in range(100):
#     folder = f"data/Tutorial{i+1}"
#     os.chmod(folder, stat.S_IWRITE)  # Make it writable
#     os.rmdir(folder)

# os.rmdir("data")

# drives = os.listdrives()
# print(drives)



# print(os.getcwd())
# print(os.getlogin())

# SYSTEM

# os.system("dir")  # Windows
# os.system("ls")   