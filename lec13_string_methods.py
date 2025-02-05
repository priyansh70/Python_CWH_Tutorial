# Strings are Immutable 
name = "Priyansh"

print(name)
print(len(name))

# It doesn't change string it returns new string 
# Convert in Uppercase 
print(name.upper())

# Convert in lowercase 
print(name.upper())

test = "!!hello!!!"
print(test)
print(test.strip("!"))
print(test.rstrip("!"))
print(test.lstrip("!"))

# Replace
print(name.replace("yan",""))

# spilt convert string into the list
fullname = "priyansh patel"
print(fullname.split(" "))

# Capitalize --> Covert Only first character into the Capital and rest all the lower
print(fullname.capitalize())

# Center Method : Alligns the string to the center as per the parameters given by the user

print(name.center(20)) #8 character already present so it adds 12 spaces equal both side
print(len(name.center(20)))
print(len(name))
print(name.center(20,"!"))
# print(len(name.center(20).strip(" ")))

# Count --> Return number of times given values has occurred within the givens string
str = "It is a testing string, It is used for the count method, it is a string which will become testing string"
print(str.count("It")) #it is case sensitive

# endswith--> Check if the string ends with given value. If yes then return true, else return false
print(str.endswith("string"))
print(str.endswith("strings"))

# We can even also check for a value in-between the string by providing start and end index positions.
print(str[:15])
print(str.endswith("testing",8,15))

# Find: Searches for the first occurrence of the givem value and return the index where it is present, if not found then return -1

print(str.find("is")) 
print(str.find("iss"))

# index: Searches for the first occurrence of the given value and returns the index where it is present. If given value is absent from the raise an exception.
# print(str.index("wwe")) #Return Exception

# isalnum: return true if the string is the alphanumeric
print(name.isalnum())

# isalpha: Only Alphabates 
print(name.isalpha())

# islower: return true if all the string in the lower case
print(name.islower())
print("priyansh".islower())
print("priyansh".isupper())

print("12".isdigit())

fullname = "The Priyansh Patel"
# istitle: Returns true only if the first letter of the each word of the string is capitalized. else return false
print(fullname.istitle())
print("the priyansh Patel".title()) #title method convert first letter in to the capital of the each word in the string

# starswith
print(str.startswith("It"))

# swapcase: It changes the characters casing of the string, Upper case are converted to lower case and lower case to upper case
print(fullname.swapcase())