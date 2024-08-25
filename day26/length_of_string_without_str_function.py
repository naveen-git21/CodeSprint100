# Returns length of string
def findLen(str):
	counter = 0
	for i in str: #this will iterate through each characters of string and then count each character
		counter += 1
	return counter


str = input("Enter a String:")
print(f"The length of the string is {findLen(str)}")
