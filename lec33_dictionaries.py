# Dictionaries: It is a ordered collection of data items, They store multiple items in a single variable. Dictionary items are key-value pairs that are separated by commas and enclosed within curly brakcets {}.

dic = {
    "name": "Priyansh",
    "age": 21,
    "eligible": True
}

print(dic["name"])  # it display error when key not found
print(dic.get("name"))

print(dic.keys())
print(dic.values())

for key in dic.keys():
    print(f"{key} = {dic[key]}")

for key, val in dic.items():
    print(f"{key} = {val}")
