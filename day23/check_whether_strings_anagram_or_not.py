# function to check if two strings are
# anagram or not 
def check(s1, s2):
	
	# the sorted strings are checked 
	if(sorted(s1)== sorted(s2)):
		print(f"The strings {s1} and {s2} are anagrams.") 
	else:
		print(f"The strings {s1} and {s2} are not anagrams.")		 
		
# driver code 
s1 ="listen"
s2 ="silent"
check(s1, s2)
