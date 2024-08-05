num = int(input("Enter a number: "))
sqrt_num = num ** 0.5
if sqrt_num.is_integer():
    print(f"{num} is a perfect square")
else:
    print(f"{num} is not a perfect square")
