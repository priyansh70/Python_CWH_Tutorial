# Manipulating Tuples 
# Tuplese are immutable, if you want to add,remove or changae tuple items, then first you must convert the tuple to a list, Then perform operation on that list and convert it back to tuple

countries = ("Spain","Italy","Finland","China")
# For Update tuple, convert it into the list
temp = list(countries)
temp.append("Australia")
temp.pop(1)
temp[0] = "England"
countries = tuple(temp)
print(countries)

# Concation two tuples, Create new tuple
t1 = (1,3,5,7,9)
t2 = (2,4,6,8,1)
numbers = t1+t2
print(numbers)

# count(): return number of times the given elements appears in the tuple
print(numbers.count(1))

# index(): Return first index of the element otherwise error
print(numbers.index(1))

# Length 
print(len(numbers))