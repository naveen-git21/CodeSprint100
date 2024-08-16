def remove_vowels(string):
    vowels = 'aeiouAEIOU'
    result = ''.join([char for char in string if char not in vowels])
    return result

# Example usage
input_string = input("Enter a string :")
result_string = remove_vowels(input_string)
print(f"The string without vowels is: {result_string}")
