def greatest(a, b, c): 

    if (a >= b) and (a >= c): 
        print(f"{a} is the greatest number")

    elif (b >= a) and (b >= c): 
        print(f"{b} is the greatest number")
    else: 
        print(f"{c} is the greatest number")
        




num1=int(input("Enter the first number: "))
num2=int(input("Enter the second number: "))
num3=int(input("Enter the third number: "))
largest=greatest(num1,num2,num3)