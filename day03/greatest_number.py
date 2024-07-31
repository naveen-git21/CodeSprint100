def comparison(num1, num2):
    if num1 > num2:
        print(f"{num1} is greater")
    elif num2 > num1:
        print(f"{num2} is greater")
    else:
        print(f"{num1} and {num2} are equal")

num1 = float(input("Enter your first number: "))
num2 = float(input("Enter your second number: "))
result = comparison(num1, num2)
