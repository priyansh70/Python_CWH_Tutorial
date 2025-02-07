# Break : The break statement Enable a program to skip over a part of the code. A break statement terminates the very loop it lies within
while True:
    num = int(input("Enter Only Even Numbers:: "))
    if(num&1):
        break
    print(num)
print("Break Loop Terminates")

# Continue : The Continue statement enable a program to skip iteration of the loop
for i in range(11):
    if(i==0):
        print("Skip the Iteration")
        continue
    print(f"5 X {i} = {5 * i}")
    
# Do While Loop Emulate in the Python
while True:
    print("It is execute, Does not even matter condition is matched or not")
    if(True):
        break
    