# Create a program capable of displaying questions to the user like KBC.
# Use List data type to store the questions and their correct answers.
# Display the final amount the person is taking home after playing the game.

kbc = {
    1: {
        "question": "Who is known as the 'God of Cricket'?",
        "options": {
            "A": "Virat Kohli",
            "B": "MS Dhoni",
            "C": "Sachin Tendulkar",
            "D": "Kapil Dev"
        },
        "answer": "C",
        "prize_money": "₹1,000"
    },
    2: {
        "question": "How many players are there in a cricket team?",
        "options": {
            "A": "9",
            "B": "10",
            "C": "11",
            "D": "12"
        },
        "answer": "C",
        "prize_money": "₹2,000"
    },
    3: {
        "question": "Which country won the first-ever Cricket World Cup in 1975?",
        "options": {
            "A": "India",
            "B": "West Indies",
            "C": "Australia",
            "D": "England"
        },
        "answer": "B",
        "prize_money": "₹3,000"
    },
    4: {
        "question": "Who was the first Indian bowler to take a hat-trick in a World Cup match?",
        "options": {
            "A": "Anil Kumble",
            "B": "Harbhajan Singh",
            "C": "Mohammed Shami",
            "D": "Chetan Sharma"
        },
        "answer": "D",
        "prize_money": "₹5,000"
    },
    5: {
        "question": "Which cricketer is known as 'Captain Cool'?",
        "options": {
            "A": "MS Dhoni",
            "B": "Virat Kohli",
            "C": "Rohit Sharma",
            "D": "Steve Smith"
        },
        "answer": "A",
        "prize_money": "₹10,000"
    },
    6: {
        "question": "Which batsman has scored the most international centuries?",
        "options": {
            "A": "Ricky Ponting",
            "B": "Virat Kohli",
            "C": "Sachin Tendulkar",
            "D": "Jacques Kallis"
        },
        "answer": "C",
        "prize_money": "₹20,000"
    },
    7: {
        "question": "Which bowler has taken the most wickets in Test cricket?",
        "options": {
            "A": "Muttiah Muralitharan",
            "B": "Shane Warne",
            "C": "James Anderson",
            "D": "Glenn McGrath"
        },
        "answer": "A",
        "prize_money": "₹40,000"
    },
    8: {
        "question": "Who hit six sixes in an over in a T20 World Cup match?",
        "options": {
            "A": "Chris Gayle",
            "B": "Yuvraj Singh",
            "C": "AB de Villiers",
            "D": "Ben Stokes"
        },
        "answer": "B",
        "prize_money": "₹80,000"
    },
    9: {
        "question": "Which team has won the most Cricket World Cups?",
        "options": {
            "A": "India",
            "B": "West Indies",
            "C": "Australia",
            "D": "England"
        },
        "answer": "C",
        "prize_money": "₹1,60,000"
    },
    10: {
        "question": "Which cricketer has scored the fastest century in ODI cricket?",
        "options": {
            "A": "AB de Villiers",
            "B": "Virender Sehwag",
            "C": "Shahid Afridi",
            "D": "Chris Gayle"
        },
        "answer": "A",
        "prize_money": "₹3,20,000"
    },
    11: {
        "question": "Who was India's first-ever Test captain?",
        "options": {
            "A": "Sunil Gavaskar",
            "B": "Kapil Dev",
            "C": "Lala Amarnath",
            "D": "CK Nayudu"
        },
        "answer": "D",
        "prize_money": "₹6,40,000"
    },
    12: {
        "question": "Who is the first cricketer to score a double century in ODIs?",
        "options": {
            "A": "Virender Sehwag",
            "B": "Rohit Sharma",
            "C": "Sachin Tendulkar",
            "D": "Martin Guptill"
        },
        "answer": "C",
        "prize_money": "₹12,50,000"
    },
    13: {
        "question": "Who is the only bowler to take 10 wickets in a single Test innings twice?",
        "options": {
            "A": "Jim Laker",
            "B": "Anil Kumble",
            "C": "Muttiah Muralitharan",
            "D": "Ajaz Patel"
        },
        "answer": "A",
        "prize_money": "₹25,00,000"
    },
    14: {
        "question": "Which Indian cricketer has won the most IPL trophies as captain?",
        "options": {
            "A": "MS Dhoni",
            "B": "Rohit Sharma",
            "C": "Virat Kohli",
            "D": "Gautam Gambhir"
        },
        "answer": "B",
        "prize_money": "₹50,00,000"
    },
    15: {
        "question": "Who scored the most runs in a single edition of an ICC Cricket World Cup?",
        "options": {
            "A": "Sachin Tendulkar",
            "B": "Ricky Ponting",
            "C": "Kane Williamson",
            "D": "Virat Kohli"
        },
        "answer": "D",
        "prize_money": "₹1 Crore"
    }
}

import time

currentQuestion = 1
totalQuestion = len(kbc)
earnedMoney = "₹0"
validOptions = ["A", "B", "C", "D"]

while currentQuestion <= totalQuestion:
    # Print Question
    print(kbc[currentQuestion]["question"])

    # Print Options
    for option, value in kbc[currentQuestion]["options"].items():
        print(f"{option}: {value}")

    # Take user Option and Validate
    userChoice = input("Choose Correct Answer's Option:: ")
    while True:
        if userChoice.upper() not in validOptions:
            print(
                f"Please choose Correct Option Valid Optiond are: {validOptions}")
            userChoice = input("Choose Correct Answer's Option:: ")
        else:
            break

    # Compare User Option with Correct Answer
    if (userChoice.strip().upper() == kbc[currentQuestion]["answer"].upper()):
        money = kbc[currentQuestion]["prize_money"]
        earnedMoney = money
        print(f"Congratulations You Won {money}")
    else:
        print("Oops!! You're answer is wrong!!")
        print(
            f"Correct Answer is Option {kbc[currentQuestion]["answer"]}: {kbc[currentQuestion]["options"][kbc[currentQuestion]["answer"]]}")
        print(f"You Won {earnedMoney} From this Show")
        break
    print("\n")
    currentQuestion += 1
