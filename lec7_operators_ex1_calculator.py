# 1. Arithmetic Operators (+, -, *, /, //, %, **)
print(15 + 6)   # Addition
print(15 - 6)   # Subtraction
print(15 * 6)   # Multiplication
print(15 / 6)   # Division (returns float)
print(15 // 6)  # Floor Division (removes decimal)
print(15 % 6)   # Modulus (remainder)
print(5 ** 3)   # Exponentiation (power)

# 2. Comparison Operators (==, !=, >, <, >=, <=)
print(10 == 5)  # Equal to
print(10 != 5)  # Not equal to
print(10 > 5)   # Greater than
print(10 < 5)   # Less than
print(10 >= 5)  # Greater than or equal to
print(10 <= 5)  # Less than or equal to

# 3. Logical Operators (and, or, not)
print(True and False)  # Returns False
print(True or False)   # Returns True
print(not True)        # Returns False

# 4. Bitwise Operators (&, |, ^, ~, <<, >>)
print(5 & 3)   # Bitwise AND
print(5 | 3)   # Bitwise OR
print(5 ^ 3)   # Bitwise XOR
print(~5)      # Bitwise NOT
print(5 << 1)  # Left shift
print(5 >> 1)  # Right shift

# 5. Assignment Operators (=, +=, -=, *=, /=, //=, %=, **=)
x = 5
x += 3  # x = x + 3
print(x)
x -= 2  # x = x - 2
print(x)
x *= 2  # x = x * 2
print(x)
x /= 2  # x = x / 2
print(x)
x //= 2  # x = x // 2
print(x)
x %= 2  # x = x % 2
print(x)
x = 5
x **= 2  # x = x ** 2
print(x)

# 6. Membership Operators (in, not in)
lst = [1, 2, 3, 4]
print(3 in lst)   # Returns True
print(5 not in lst)  # Returns True

# 7. Identity Operators (is, is not)
a = [1, 2, 3]
b = a
c = [1, 2, 3]
print(a is b)     # True (same object)
print(a is c)     # False (different objects)
print(a is not c)  # True
