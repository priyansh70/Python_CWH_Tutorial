# Finally 
# It is a part of exception handlinhg, When we handle execption using the try and except block, we can include a finally block at the end. The finally block is always executed, so it is genrally used for doing the concluding tasks like closing file resources or closing database connections or may be ending the program execution with a delightful message

try:
    l = [1,3,5,6,7]
    idx = int(input("Enter Index: "))
    print(l[idx])
except:
    print("Some Error Occurred")
finally:
    print("This code is always execute")