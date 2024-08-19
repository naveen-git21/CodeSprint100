# Python program to check whether a character is alphabet or not

print ("Enter a character to check itself: ", end="")
char = str (input ())[0]

if (char >= 'a' and char <= 'z') or (char >= 'A' and char <= 'Z'):
    print (char, "is an alphabet character.")
else:
    print (char, "is not an alphabet character.")