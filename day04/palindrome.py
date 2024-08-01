def palindrome(str):
    for i in range(0, int(len(str) / 2)):
        if str[i] != str[len(str) - i - 1]: 
            # this will compare the elements from the first and from the last 
            return False
    return True

# Example usage:
input = input("Type a word:")
if palindrome(input):
    print("Yes, it's a palindrome.")
else:
    print("No, it's not a palindrome.")
