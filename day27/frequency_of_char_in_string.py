def frequency(st,check):
    count=0
    st = st.lower()  # Convert the string to lowercase
    check = check.lower()
    for i in st:
        if check == i:
            count+=1
            
    return count

print("Check the frequency of a character")
print("#"*40)
st = input("Enter a string: ")
check =input("Enter the character to check frequency:")[0]
print(f"{check} has the frequency of {frequency(st,check)}")