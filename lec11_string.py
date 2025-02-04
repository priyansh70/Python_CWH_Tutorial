firstname = "Priyash"
lastname = 'patel'
fullname = firstname+" "+lastname

print(fullname)

# Multi Line String 
multi_line_string1 = """
It is a multi 
line string with
double quote
"""

multi_line_string2 = '''
It is a multi 
line string with
single quote
'''

print(multi_line_string1)
print(multi_line_string2)

# Indexing in the String
# print(fullname[40]) Index out of the bond
# print(fullname[0])

# Iterate single character with for loop 
for char in fullname:
    print(char)