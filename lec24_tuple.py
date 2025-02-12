# Tuple: It is similar to the Lists but it is unchangeable we can not alter them after creation

# If in the tuple only one element present so we must give comma, otherwise it is consider int
# t = (1,) 

t = (1,2,True,"Priyansh")
print(type(t),t)

# Positive Indexing 
print(t[0])
print(t[1])
print(t[2])
print(t[3])

# Negative Indexing 
print(t[-4])

if 1 in t:
    print("Present")

# Return new tuple when slicing perform
nt = t[-3:-1]
print(nt)