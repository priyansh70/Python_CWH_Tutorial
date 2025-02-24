# Enumerate Function 
# It is a function is a built in function in python that allows you to loop over a sequence(such as a list,tuple, or string) and get the index and value of each element in the sequence at the same time.

marks = [10,5,6,4,80,90,50]

for index,mark in enumerate(marks):
    print(f"{index} : {mark}")
    print("You're Fail") if mark < 33 else print("You're Pass!!")
    if(index == 4):
        print("Condition")
