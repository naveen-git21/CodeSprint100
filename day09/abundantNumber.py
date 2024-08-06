""" if the sum of all the proper divisors of the number denoted by sum(n)
is greater than the value of the number n """

num=int(input("Enter a number: "))
sum = 0
# iterating loop n times
for i in range(1, num):
    # finding proper divisors
    if num % i == 0:
        # adding proper divisors to the sum s
        sum += i
# checking if sum is greater than the
# given number then it is called
# anundant so print yes otherwise no
if sum > num:
    print(f"{num} is a abundant number")
else:
    print(f"{num} is not a abundant number")