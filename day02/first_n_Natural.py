def sum_of_N(n):
    return int((n/2)*(n+1))
    
print("Sum of first of N natural numbers")
num=int(input("Enter a number :"))

if(num<0):
    print("Enter a positive number")
else:
    result = sum_of_N(num)
    print("The sum of first n Natural numbers upto ",num,"is",result)