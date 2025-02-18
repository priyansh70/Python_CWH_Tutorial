# Methods of the Set 
s1 = {1,2,3,5,7,9}
s2 = {2,3,4,6,8}

# Union: Merge Both Sets 
print(s1.union(s2))

# Interect: Print Comman Items
print(s1.intersection(s2))

# We can use update method for updating one set
# Example 
cities = {"Tokyo","NY"}
cities2 = {"Delhi","Indore"}

cities.update(cities2) #It merge in the cities
print(cities)

cities.intersection_update(cities2)
print(cities)

# Symmetric Difference: All the Unique values in the 2 sets, or we can say that Union - Intersection
print(s1.symmetric_difference(s2))

# Difference: A-B (Elements present in the Set B and Set A not include in the Difference)
print(s1.difference(s2))

# isdisjoint: Methods checks if items of given set are present in another set. This methods return False if items are present, else it return True 
print(s1.isdisjoint(s2))
s3 = {10,20,40,30}
print(s1.isdisjoint(s3))

# SuperSEt : if all items are present in the particular set, Return true if, otherwise False
print(cities.issuperset(cities2))
print(cities.issubset(cities2))


# ADD :Add item in the Set
test = {1,4,6,8}
print(test)

test.add(5)
print(test) #Add Items in the SEt

test.discard(5)
print(test) #Discard Remove Items From the Set, If Present

# test.remove(5)
print(test) #Remove remove Items From the Set, If Present otherwise throws error

# Pop: This methods remove the last items of the set but catch is that we don't know which item gets popped as sets are unordered.
print(cities)
print(cities.pop())
print(cities)
 
# Del : It is keyword which deletes the set entirely
del cities

# Clear: This methods clears all the items from the sets
cities2.clear()
print(cities2)