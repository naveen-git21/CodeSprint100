# If a number is divisible by the sum of its digits, then it will be known as a Harshad Number.
# The number 156 is divisible by the sum (12) of its digits (1, 5, 6 ).

num=int(input("Enter a number: ")) 
rem = sum = 0;    
     
#Make a copy of num and store it in variable n    
n = num;    
     
#Calculates sum of digits    
while(num > 0):    
    rem = num%10;    #extract the last digit from the number
    sum += rem;    
    num = num//10;    #update the number with removing the last digit
     
#Checks whether the number is divisible by the sum of digits    
if(n%sum == 0):    
    print(f"{n} is a harshad number");    
else:    
    print(f"{n} is not a harshad number");    