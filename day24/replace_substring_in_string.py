def replaceABwithC(input_string, pattern, replace_with): 
    return input_string.replace(pattern, replace_with) 

# Driver program 
if __name__ == "__main__": 
    input_string = "This is an ACM Coding event"
    print("Original string:", input_string)
    
    pattern = input("Enter the substring you want to replace: ")
    replace_with = input("Enter the new substring: ")
    
    result = replaceABwithC(input_string, pattern, replace_with)
    print("Modified string:", result)
