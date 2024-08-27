rows = int(input("Please Enter the Total Number of Rows: "))
columns = int(input("Please Enter the Total Number of Columns: "))

print("Hollow Rectangle Star Pattern")
print()
i = 0
while i < rows:
    j = 0
    while j < columns:
        if i == 0 or i == rows - 1 or j == 0 or j == columns - 1:
            print('*', end='  ')
        else:
            print(' ', end='  ')
        j += 1
    print()
    i += 1

print()