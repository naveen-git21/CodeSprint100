def factorial(num):
    if num < 0:
        print("Sorry, factorial does not exist for negative numbers")
    elif num == 0:
        print("The factorial of 0 is 1")
    else:
        result = 1
        for i in range(1, num + 1):
            result *= i
        print(f"The factorial of {num} is {result}")

print("Palindrome")
input = int(input("Enter a number:"))
factorial(input)