# age = int(input("Enter Your Age: "))

# Conditional Operators 
# >, <, >=, <=, !=, ==
# print(age>18)
# print(age>=18)
# print(age<18)
# print(age<=18)
# print(age==18)
# print(age!=18)

# If Else 

# if(age >18):
#     print("You can Drive!!!")
# else:
#     print("You Can't Drive")
    
# If Elif Else and Nested If Else 
num = int(input("Enter Number: "))

if(num < 0):
    print("Entered Number is Negative")
elif(num == 0):
    print("Entered Number is Zero")
else:
    print("Entered Number is Posivive")
    if(num % 2):
        print("Entered Number is Odd")
    else:
        print("Entered Number is Even")
    