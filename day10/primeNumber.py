#Prime number or not

num = int(input("Enter a number : "))

# Negative numbers, 0 and 1 are not primes
if num > 1:
  
    # Iterate from 2 to n // 2
    # no number greater than n/2 can divide the number n ,so we iterate till (n/2)+1
    for i in range(2, (num//2)+1):
      
        # If num is divisible by any number between 2 and n / 2, it is not prime
        if (num % i) == 0:
            print(num, "is not a prime number")
            break #if some number id dividing we no need to check all number , so break the loop
    else:
        print(num, "is a prime number")
else:
    print(num, "is not a prime number")