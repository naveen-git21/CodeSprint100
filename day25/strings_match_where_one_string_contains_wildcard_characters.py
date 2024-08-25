# strings match where one string contains wildcard characters
# Python program to match wild card characters 

# The main function that checks if two given strings match. 
# The first string may contain wildcard characters 


def match(first, second): 

	# If we reach at the end of both strings, we are done 
	if len(first) == 0 and len(second) == 0: 
		return True

	# Make sure to eliminate consecutive '*' 
	if len(first) > 1 and first[0] == '*': 
		i = 0
		while i+1 < len(first) and first[i+1] == '*': 
			i = i+1
		first = first[i:] 

	# Make sure that the characters after '*' are present 
	# in second string. This function assumes that the first 
	# string will not contain two consecutive '*' 
	if len(first) > 1 and first[0] == '*' and len(second) == 0: 
		return False

	# If the first string contains '?', or current characters 
	# of both strings match 
	if (len(first) > 1 and first[0] == '?') or (len(first) != 0
												and len(second) != 0 and first[0] == second[0]): 
		return match(first[1:], second[1:]) 

	# If there is *, then there are two possibilities 
	# a) We consider current character of second string 
	# b) We ignore current character of second string. 
	if len(first) != 0 and first[0] == '*': 
		return match(first[1:], second) or match(first, second[1:]) 

	return False

# A function to run test cases 


def test(first, second): 
	if match(first, second): 
		print("Yes") 
	else: 
		print("No") 


# Driver program 
test("g*ks", "geeks") # Yes 
test("ge?ks*", "geeksforgeeks") # Yes 
test("g*k", "gee") # No because 'k' is not in second 
test("*pqrs", "pqrst") # No because 't' is not in first 
test("abc*bcd", "abcdhghgbcd") # Yes 
test("abc*c?d", "abcd") # No because second must have 2 instances of 'c' 
test("*c*d", "abcd") # Yes 
test("*?c*d", "abcd") # Yes 
test("geeks**", "geeks") # Yes 

# This code is contributed by BHAVYA JAIN and ROHIT SIKKA 
