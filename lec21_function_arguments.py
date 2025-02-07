# Function Arguments and return statement
# 4 Types of of Arguments

# 1 -- Default 
# If Parameter not passed while calling the function, so it takes default value of the argument, if set.

def name(firstname,middlename="Singh",lastname="Sidhu"):
    print("Good Morning,",firstname,middlename,lastname)
    
name("Navjot")
name("Navjot",lastname="Patel")
name("Navjot",middlename="The")
name("Navjot","The","Patel")

# 2 -- Keyword Argument
# We can provide arguments with key = value, this way the interpreter recognized the arguments by the parameter name. Hence, the order in which argumentes are passed does not matter.
name(middlename="The",firstname="Priyansh",lastname="Patel")

# 3 -- Variable Length Argument
def addNumbers(*numbers):
    sum = 0
    for i in numbers:
        sum += i
    print("Sum:: ",sum)

addNumbers(1,2,65,44,64,4)

# Take Dictionary in the Argument
def fullname(**name):
    print(type(name))
    print("Hello,",name["fname"],name["mname"],name["lname"])
    
fullname(fname="Daren",mname="Singh",lname="Sammy")

# 4 -- Required Argument
# In case we don't pass the arguments with a key=value syntax, then it is necessary to pass the arguments in the correct positional order and the number of argumemtes passed should match with actual function definition

def printname(fname,mname,lname):
    print("Good Morning,", fname,mname,lname)

# printname("Peter","Quill") #Throw Error because one parameter missing


# Return Value in the Function 
def average(*numbers):
    sum = 0
    for num in numbers:
        sum += num
    return sum/len(numbers)

print("Average is:: ",average(10,20,30,40))