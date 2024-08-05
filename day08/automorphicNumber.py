num = int(input("Enter a number you want to check: "))  
  
#calculating the number of digits  
num_of_digits = len(str(num))  
  
#computing the square of a number  
square = num**2  
  
#obtaining the last digits   
last_digits = square%pow(10,num_of_digits)  # this pow function will give the 10 raised to the power of the followed number(num_of_digits)
  
#comparing the digits of number with input  
if last_digits == num:  
  print(f"Yes, {num} is an automorphic number")  
else:  
  print(f"No, {num} is not an automorphic number")  