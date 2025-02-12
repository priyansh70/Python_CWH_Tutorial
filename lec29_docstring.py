# Docstring: Python docstring are the string literals that appear right after the definition of a function, method, class or module

# --> It is write a just after the definition of a funciton,module, class or method, they are associated with the object as their doc attribute. We can later use this attribute to retrieve this docstring

def sqaure(n):
    """Takes in a number n, and return the sqaure of the number n"""
    
    return n**2

print(sqaure(2))
print(sqaure.__doc__)

# Pep8 
# --> It is a guidline of the python program (Python Enhance Document)