def reverse(number):
    original_number = number
    reverse = 0
 
    while number > 0:
        digit = number % 10 #get the last digit of the number
        reverse = reverse * 10 + digit # add the digit to the reverse 
        number //= 10 #update the number after removing the digit
        
 
    print(f"Reversed Number: {reverse}")
 
# Example Usage
input = int(input("Enter the number: "))
reverse(input)