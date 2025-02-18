# Raising Custom Error 
a = input("Enter the value between 5 and 9 : ")

if(a == "quit"):
    print("Thank You")
elif(int(a)<5 or int(a)>9):
    raise ValueError("The given item is invalid")
print("You Have a Great Day")