# While Loop: Execute statements while the condition is True. As soon as the condition becomes False, the interpreter comes out of the While Loop 

i = 1
while(i<=3):
    print(i)
    i += 1
# Else with While Loop
else:    
    print("Out of Loop")

# Random Number Guess Between 1 - 100 
import random
mini = 1
maxi = 100
attempt = 0
user_guess = -1
random_number = random.randint(mini,maxi)


while(random_number != user_guess):
    user_guess = int(input("Guess the Number:: "))
    if(user_guess < mini or user_guess > maxi):
        print(f"Please Guess the Number between ({mini},{maxi})")
    elif(user_guess == random_number):
        print("You guess the number")
    elif(user_guess > random_number):
        print("You Guess Bigger Number than the Actual")
    else:
        print("You Guess the Lesser Number than the Actual") 
    attempt += 1   

# Rank based on the Attempts User takes
if attempt <= 3:
    print("Your are Genius!!!")
elif attempt <= 5:
    print("You are Smart")
elif attempt <= 7:
    print("You are Not Good")
else:
    print("So Dumb!!")

# Do While Loop: --> Do while loop not exists in the Python, But we can Create our own by using continue and break
while True:
    num = int(input("Enter a number (Enter 0 to stop): "))
    if num == 0:
        break  # Exit loop when the user enters 0
    print(f"You entered: {num}")

