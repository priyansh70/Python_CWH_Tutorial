# Execption Handling 
# It is the process of responding to unwantend or unexpected events when a computer program runs. Exception handling deals with these events to avoid the program or system crashing, and without this process, execptions would disrupts the normal operation of a program

num = input("Enter the Number: ")
print(f"Multiplication table of {num} is: ")

try:
    for i in range(1,11):
        print(f"{int(num)} X {i} = {int(num) * i}")
except:
    print("Invalid Input")

print("Important Lines of Code!!!")
print("End of the Program")

# ----------------- 

# Catch Specific Exception 
try:
    idx = int(input("Enter any number: "))
    arr = [2,4,6]
    print(arr[idx])
except ValueError:
    print("Invalid Input Type")
except IndexError:
    print("Index out of bound")
