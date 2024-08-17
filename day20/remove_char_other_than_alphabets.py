def removeAll(input): 

	# Traverse complete string and separate 
	# all characters which lies between [a-z] or [A-Z] 
	sepChars = [char for char in input  #takes each and every element of the string 
            	if ord(char) in range(ord('a'),ord('z')+1,1) or #compares the ASCII value of char in range of ASCII value of a to  z
                ord(char) in range(ord('A'),ord('Z')+1,1)]  #compares the ASCII  value of char in range of ASCII value of A to  Z

	# join all separated characters 
	# and print them together 
	return ''.join(sepChars) 

# Driver program 
if __name__ == "__main__": 
	input = input("Enter the string: ")
	print (removeAll(input)) 
