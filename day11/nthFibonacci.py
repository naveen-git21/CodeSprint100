def fibonacci(n):
    # function for finding the fibonacci number
    a = 0
    b = 1
    if n < 0:
        print("Incorrect input")
    elif n == 0:
        return a
    elif n == 1:
        return b
    else:
        for i in range(2, n+1):
            c = a + b
            a = b
            b = c
        return b

print("Fibonacci number")
num=int(input("Enter a number and find its fibonacci number: "))
result=fibonacci(num)
print(f"the fibonacci number of {num} is {result}")