def sum_in_range(start, end):
    sum = 0
    for i in range(start, end + 1):
        sum += i
    return sum

print("Sum of numbers in range")
start = int(input("Enter the start of the range: "))
end = int(input("Enter the end of the range: "))

result = sum_in_range(start, end)
print(f"Sum of numbers from {start} to {end} is: {result}")
