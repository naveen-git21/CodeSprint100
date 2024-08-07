# Python program to display all the prime numbers within an interval

lower = int(input("Enter the lower range :"))
upper = int(input("Enter the upper range :"))

print(f"Prime numbers between{lower}and{upper}are:")

for num in range(lower, upper + 1):
   # all prime numbers are greater than 1
   if num > 1:
       for i in range(2, int(num/2)):
           if (num % i) == 0:
               break
       else:
          print(num)