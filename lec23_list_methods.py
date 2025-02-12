l = [12,24,12,5]
print(l)

# Add Itme in the List
l.append(20)
print(l)

# Sort the List Items
l.sort() #Ascending Order
l.sort(reverse=True) #Descending Order

#Reverse the List
l.reverse()
print(l) 

# index: Return element index otherwise error
print(l.index(12))

# Count Method: Return count of the element occurence
print(l.count(12))

# In the python If assign list to new list, then changed in the new list so existing list also changed.
# For avoid this, we have to use copy method
nl = l
nl[0] = 1
print(nl)
print(l)

# Copy
nl2 = l.copy()
nl2[0] = 10
print(nl2)
print(l)

# Insert: Add new item at specific index
l.insert(12,50) #index,item
print(l)

# Extend Method: This methods adds an entire list or any other collection datatype(set,tuple,dictionary) to the existing list
colors = ["voilet","indigo","blue"]
rainbow = ["green","yellow","red","orange"]
more_color = ("black","white")
print(colors)

colors.extend(rainbow)
colors.extend(more_color)
print(colors)

# Concatenating two lists
# Old List Does not modify 
newlist = colors + rainbow
print(newlist)
