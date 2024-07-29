def classify(num):
    if num == 0:
        print("Neither positive nor negative")
    elif num > 0:
        print("Positive")
    else:
        print("Negative")


print("Positive or Negative")
scan = int(input("Enter the number: "))
classify(scan)
    
