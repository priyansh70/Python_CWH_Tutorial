# Recursion: It is the process of defining something in terms of itself.
# Call function itself

# function(5) = 5*4*3*2*1
# function(4) = 4*3*2*1

# function(n) = n * function(n-1)

def factorial(n):
    if(n==0 or n==1):
        return 1
    return n * factorial(n-1)

print(factorial(5))

# Fibonacci Series
def fibonacci(n):
    if(n == 0):
        return n
    elif(n == 1):
        return n
    else:
        ans = fibonacci(n-1) + fibonacci(n-2)
        # print(ans)
        return ans
print(fibonacci(18))

