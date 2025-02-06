num = int(input("Enter Week Day Number:: "))

match num:
    case 1:
        print("Monday")
    case 2:
        print("Tuesday")
    case 3:
        print("Wednesday")
    case 4:
        print("Thursday")
    case 5:
        print("Friday")
    case 6:
        print("Saturday")
    case 7:
        print("Sunday")
    case _:
        print("Not Valid Day")

# Matching Coordinates  
x = int(input("Enter X Coordinate:: "))
y = int(input("Enter Y Coordinate:: "))

match (x,y):
    case (0,0):
        print("Origin Point")
    case (0,y):
        print(f"Y-Axis at {y}")
    case (X,0):
        print(f"X-Axis at {x}")
    case (x,y):
        print(f"Points at ({x},{y})")
    case _:
        print("Invalid Coordinates")