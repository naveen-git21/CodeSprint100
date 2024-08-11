def power(N,x):
    result=N**x
    return result

print("Power of a number")
print("*"*20)

num,expo=map(int,input("Enter the number and the power :").split())
print(f"The result of {num} raised to the power {expo } is {power(num,expo)}")