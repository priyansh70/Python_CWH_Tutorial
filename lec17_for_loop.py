# For Loop : Can Iterate over a sequence of iterable objects in python. Iterating over a sequence ins nothing but over string, lists, tuple, sets and dictionaries

# Iterating in the string 
name = "Priyansh"
for ch in name:
    print(ch,end=", ")
print('\n')
    
# # Iterating in the List 
colors = ["red","yellow","pink","black","white"]
# for color in colors:
#     print(color, end=" || ")
# print("\n")

# Iterating Nested Loop 
for color in colors:
    print(color)
    for ch in color:
        print(ch,end=", ")
    print("\n")

# Loop in Range 
for i in range(10):
    print(i)
    
print("\n") 
    
for i in range(1,101):
    print(i)

for i in range(1,101,4):
    print(i)

