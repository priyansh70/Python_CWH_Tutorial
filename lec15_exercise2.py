import time

morning_time = 5
afternoon_time = 12
evening_time = 17
night_time = 21
current_time = int(time.strftime("%H"))

if(current_time >= morning_time and current_time < afternoon_time):
    print("Good Morning Dost!!!")
elif(current_time >= afternoon_time and current_time < evening_time):
    print("Good Afternoon Dost!!!")
elif(current_time >= evening_time and current_time < night_time):
    print("Good Evening Dost!!!")
else:
    print("Good Night Dost!!!")
