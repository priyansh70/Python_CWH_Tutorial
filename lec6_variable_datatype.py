# Variable: it is like a container that holds data.
# Creating a variable is like creating a placeholder is memory and assigning it some value.

a = 26455
print(a)

b = "Priyansh"
print(b)

# DataType: It specifies the type of value a variable holds. This is required in programming to do various operations without causing error.
# We can print the type of any operator using type function

c = True
print(c)

d = None 
print(d)

e = 1.1
print(e)

f = complex(8,2)
print(f)

# Types 
print("The Type of a is: ",type(a))
print("The Type of b is: ",type(b))
print("The Type of c is: ",type(c))
print("The Type of d is: ",type(d))
print("The Type of e is: ",type(e))
print("The Type of f is: ",type(f))

# List 
test_list = [1,3,4,"priyansh"]
print(test_list)
print("The Type of test_list is: ",type(test_list))


# Tuple 
test_tuple = ("priyansh","patel")
print(test_tuple)
print("The Type of test_tuple is: ",type(test_tuple))

# Dictionary 
test_dict = {
    "name" : "priyansh",
    "age" : 21
}
print(test_dict)
print("The Type of test_dict is: ",type(test_dict))