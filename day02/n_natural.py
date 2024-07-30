def sum_of_N(init,end):
    total=(end/2)*(end+1)
    init-=1
    to_reduce=(init/2)*(init+1)
    sum =total - to_reduce
    return int(sum)
    
    
print("Sum of N natural numbers")
init=int(input("Enter starting number :"))
end=int(input("Enter ending number :"))

if(init and end <0):
    print("Enter a positive number")
else:
    result = sum_of_N(init,end)
    print("The sum of n Natural numbers from",init,"to",end,"is",result)