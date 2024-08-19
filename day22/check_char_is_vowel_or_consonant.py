def check_vowel_or_consonant(char):
    # Ensure the input is a single alphabetic character
    if len(char) == 1 and char.isalpha():
        # Define vowels
        vowels = 'aeiouAEIOU'
        
        # Check if the character is a vowel
        if char in vowels:
            return f"{char} is a vowel."
        else:
            return f"{char} is a consonant."
    else:
        return f"{char} is not a valid single alphabet character."

# Get user input
char = input("Enter a character to check: ")
print(check_vowel_or_consonant(char))
