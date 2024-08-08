def factors(n):
    print(f'the factors of {n} are :')
    # no number greater than n/2 can the number n 
    for i in range(1,int(n/2)+1): # here the iteration have been reduce upto n/2 
        if n%i ==0:
            print(i)
    print(n) # since the iteration have been reduced we need to print he original number alone
    
num=int(input("Enter the number to find its factors: "))
result=factors(num)