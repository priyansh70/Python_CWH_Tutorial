# List 
# --> Lists are ordered collection of data items.
# --> They store multiple items in a single variable
# --> List items are sepearated by commas and enclosed within square brackets [].
# --> Lists are changeble meaning we can alter them after creation

marks = [3,5,7]
print(marks)
print(type(marks))
print(marks[0])
print(marks[1])
print(marks[2])
# print(marks[3])  #Error

# Any types of variable could be inside the lists
t_list = [1,"String",True,('t','u','p','l','e'),["List","Inside","List"]]
print(t_list)

# Negative Indexing 
print(marks[-3])

if 7 in marks:
    print("Yes, It is Present")
else:
    print("Absent")

# Same Things Apply for String as well
if "man" in "Roman":
    print("Yes, It is present")

# Print All 

num = [1,3,6,5,85,98,4,1,2,12,6,5,20]
print(num)
print(num[:])
print(num[1:-1])
print(num[2:-3:2]) #Jump Index

# List Comprehension
# --> List comprehensions are used for creating new lists from other iterables like lists, tuples, dictionaries, sets, and even in arrays and strings

newlist1 = [i*i for i in range(1,10)]
print(newlist1)
newlist2 = [i*i for i in range(1,10) if i%2 == 0]
print(newlist2)