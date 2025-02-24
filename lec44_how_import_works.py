# Importing in python is the process of loading code from a Python module into the current script.

import math
print(math.floor(4.3424))
print(math.sqrt(4))

# # We can import specific functino or variable by from keyword 
# from math import pi,sqrt
# print(pi)
# print(sqrt(4))


# Import Everything  [Not Recommended]
# from math import * 

# As Keyword 
import math as m
# from math import sqrt as s

# dir
print(dir(math))
print(type(math.__doc__))