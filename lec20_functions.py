# Function : It is a piece of code that peform specific task whenever it is called. used in multiple times in program and write once

# Two types of functions 

# 1 -- built in function 
# These function are defined and pre coded in python. Some Example:  min(),max(),len(),print(),range(),sum(),etc

# 2 -- user defined function
# We can create functions to perform specific tasks as per our needs. Such functions are called user-defined functions.


# Example : Function for calculate GMean
def calculateGmean(a,b):
    mean = (a*b)/a+b
    print(mean)
    
def isGreater(a,b):
    if(a>b):
        print("First Number is Greater")
    else:
        print("Second Number is Greater")
  
def someFunction(a,b):
    pass #it is used for the pass the body at definition time  
  
a = 10
b = 20
c = 15
d = 25

calculateGmean(a,b)
isGreater(c,d)

calculateGmean(a,b)
isGreater(c,d)

# Built in 

print(sum((a,b)))
print(min((a,b)))

