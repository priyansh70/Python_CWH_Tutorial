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
        

user_string = input("Enter Message:: ")
words = user_string.split(" ")

try:
    choice = input("For Code Enter Press 1: \nFor Decode Enter Press 2: \n")
    while True:
        if choice not in ['1','2']:
            print(
                f"Please choose Correct Option Valid Options are: {['1','2']}")
            choice = int(input("For Code Enter Press 1: \nFor Decode Enter Press 2: \n"))
        else:
            break
except:
  print("Something went wrong")
  
match choice:
    case '1':
        coded_words = []
        for word in words:
            if(len(word) <= 3):
                code = word[::-1]
                coded_words.append(code)
            else:
                start_code = randomCharacters()
                end_code = randomCharacters()
                
                code = start_code + word[1:] + word[0] + end_code
                coded_words.append(code)
        print(" ".join(coded_words))
                
    case '2':
        decoded_word = []
        for word in words:
            if(len(word) <= 3):
                decode = word[::-1]
                decoded_word.append(decode)
                
            else:
                decode = word[3:-3]
                decode = decode[-1] + decode[:-1]
                decoded_word.append(decode)
        print(" ".join(decoded_word))
            
    case _:
        print("Invalid Options")