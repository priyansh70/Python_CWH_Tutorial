# Update: If items present then it update otherwise new item added

info = {
    "name": "Priyansh",
    "age": 21,
    "eligible": True
}
print(info)
info.update({"age": 22})

info.update({"DOB": 1643})
print(info)

info.pop("DOB") #Remove Specific Item from the Dict, If not present it gaves error
print(info)

info.popitem() #Remove Last Item
print(info)

# del keyword --> Delete Dictionary
info1 = {
    "name": "Priyansh",
    "age": 21,
    "eligible": True
}
del info1
print(info1)

# Clear
info.clear()
print(info)
