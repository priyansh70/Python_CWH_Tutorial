# It is used previosly 
name = "Priyansh"
country = "India"

letter1 = "Hey My Name is {} and I am from {}"
letter2 = "Hey My Name is {1} and I am from {0}"
print(letter1.format(name,country))
print(letter2.format(country,name))

# F String 
print(f"Hey My Name is {name} and I am from {country}")

num1=10.5968
num2=20.203
print(f"Number 1: {num1} + Number 2: {num2} = Sum: {num1+num2 : .2f}")
print(f"Number 1: {{num1}} + Number 2: {{num2}} = Sum: {{num1+num2 : .2f}}")
