sum=0   
num=int(input("Enter a number:"))  
# temporary variable  store copy of the original number  
temp=num  
 
while(num):  
    # intialize with 1  
    i=1  
    fact=1  
    rem=num%10  
    
    while(i<=rem):  
        fact=fact*i   # Find factorial of each number  
        i=i+1  
    sum=sum+fact  
    num=num//10  
if(sum==temp):  
    print(f"{temp} is a strong number")  
else:  
    print(f"{temp}  is not a strong number")  