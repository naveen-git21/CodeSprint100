def count_vowels(string):
    vowels = 'aeiou'
    string = string.lower()
    count = {vowel: 0 for vowel in vowels}
    total = 0
    for char in string:
        if char in count:
            count[char] += 1
            total += 1
    
    return count, total


input_string = input("Enter a string :")
vowel_count, total_count = count_vowels(input_string)
print(f"The number of vowels is {total_count} and the count of each vowels is {vowel_count}")
