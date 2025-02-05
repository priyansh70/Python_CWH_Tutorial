# Exercise: Create a Calculator Solution
"""
Create a calculator capable of performing addition, substraction, multiplication, and division operations on two numbers. your program should format the output in a readable manner 
"""

print("It is Basic Calculator!!")

while True:
    print("Which Operation Do you want to Perform?\n1 --> Addition\n2 --> Substraction\n3 --> Multiplication\n4 --> Division\n0 --> Exit")
    operation = float(input("Enter Operation Number:: "))


    if(operation == 0):
        break
    
    if(operation > 4 or operation < 0):
        print("Please Enter Valid Operation Number")
        continue

    first_number = float(input("Enter First Number:: "))
    second_number = float(input("Enter Second Number:: "))


    if operation == 1:
        sum = first_number + second_number
        print(f"{first_number} + {second_number} = {sum}\n")
        
    elif operation == 2:
        sub = first_number - second_number
        print(f"{first_number} - {second_number} = {sub}\n")
        
    elif operation == 3:
        multipliy = first_number * second_number
        print(f"{first_number} * {second_number} = {multipliy}\n")
        
    else:
        div = first_number / second_number
        print(f"{first_number} / {second_number} = {div}\n")