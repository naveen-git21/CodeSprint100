def reverse(number):
    sum = 0
 
    while number > 0:
        digit = number % 10 #get the last digit of the number
        cube= digit**3 #cube the digit
        sum +=cube # add the cubed number of the digit
        number //= 10 #update the number after removing the digit
        
    return sum
 
# Example Usage
input = int(input("Enter the number: "))
if input==sum:
    print(f"{input} is an armstrong number")
else:
    print(f"{input} is not an armstrong number")