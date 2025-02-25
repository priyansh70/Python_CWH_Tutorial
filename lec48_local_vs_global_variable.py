x = 10

def func():
    global x
    x = 5
    y = 51
    
    print(y)
    
func()
print(x) #value changed
# print(y) #not access, it is local var