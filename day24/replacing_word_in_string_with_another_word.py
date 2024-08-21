def replace_word(input_string, word, replace_with):
    return input_string.replace(word, replace_with) 

# Driver program
if __name__ == "__main__":
    input_string = "This is an ACM Coding event"
    print("Original string:", input_string)
    
    # Get the first word from user input
    pattern = input("Enter the word you want to replace: ").split()[0].strip()
    replace_with = input("Enter the replacement word: ").split()[0].strip()
    
    result = replace_word(input_string, pattern, replace_with)
    print("Modified string:", result)
