# Write a python program to translate a message into secret code language. Use the rules below to translate normal English into secret code language

# Coding:
# if the word contains atleast 3 characters, remove the first letter and append it at the end
#   now append three random characters at the starting and the end
# else:
#   simply reverse the string

# Decoding:
# if the word contains less than 3 characters, reverse it
# else:
#   remove 3 random characters from start and end. Now remove the last letter and append it to the beginning

# Your program should ask whether you want to code or decode

"""Solution Starts"""
 
import random
def randomCharacters():
    # Combine all characters into a single list
    # Generate lists for each category
    lowercase_letters = list("abcdefghijklmnopqrstuvwxyz")  # a-z
    uppercase_letters = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")  # A-Z
    digits = list("0123456789")  # 0-9
    special_characters = list(
        "!\"#$%&'()*+,-./:;<=>?@[]^_`{|}~")  # Special characters

    # Combine all characters into a single list
    all_characters = lowercase_letters + uppercase_letters + digits + special_characters
    temp_char = []
    
    for i in range(3):
        idx = random.randint(0,len(all_characters)-1)
        temp_char.append(all_characters[idx])
        
    code = "".join(temp_char)
    return code
        
# --------    
   
print("Welcome in the Code and Decode Your Word!!")
print("What you want to do?")

user_string = input("Enter String:: ")

try:
    userChoice = input("For Code Enter Press 1: \nFor Decode Enter Press 2: \n")
    while True:
        if userChoice not in ['1','2']:
            print(
                f"Please choose Correct Option Valid Options are: {['1','2']}")
            userChoice = int(input("For Code Enter Press 1: \nFor Decode Enter Press 2: \n"))
        else:
            break
except:
  print("Something went wrong")
  
match userChoice:
    case '1':
        if(len(user_string) <= 3):
            code = user_string[::-1]
            print("You String is Coded Now:: ",code)
        else:
            user_str = user_string.swapcase()
            start_code = randomCharacters()
            end_code = randomCharacters()
            
            code = start_code + user_str[1:] + user_str[0] + end_code
            print(code)
            
    case '2':
        if(len(user_string) <= 3):
            decode = user_string[::-1]
            print("You String is Decoded Now:: ",decode)
            
        else:
            decode = user_string[len(user_string)-4] + user_string[3:len(user_string)-4]
            print(decode.swapcase())
            
    case _:
        print("Invalid Options")