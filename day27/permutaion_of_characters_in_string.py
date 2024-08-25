# Python3 Program to print all permutations
# of a string in sorted order.

# The following function is needed for the sort method


# This function finds the index of the smallest character
# which is greater than 'first' and is present in str[l..h]
def findCeil(str_, first, l, h):

	# initialize index of ceiling element
	ceilIndex = l

	# Now iterate through rest of the elements and find
	# the smallest character greater than 'first'
	for i in range(l + 1, h + 1):
		if (str_[i] > first and str_[i] < str_[ceilIndex]):
			ceilIndex = i

	return ceilIndex


# Print all permutations of str in sorted order
def sortedPermutations(str_):

	# Get size of string
	size = len(str_)

	# Sort the string in increasing order
	str_ = sorted(str_)

	# Print permutations one by one
	isFinished = False
	while (isFinished is False):

		# print this permutation
		print("".join(str_))

		# Find the rightmost character which is
		# smaller than its next character.
		# Let us call it 'first char'
		i = size - 2
		while i >= 0:
			if (str_[i] < str_[i+1]):
				break
			i -= 1

		# If there is no such character, all are
		# sorted in decreasing order, means we
		# just printed the last permutation and we are done.
		if (i == -1):
			isFinished = True
		else:

			# Find the ceil of 'first char' in
			# right of first character.
			# Ceil of a character is the smallest
			# character greater than it
			ceilIndex = findCeil(str_, str_[i], i + 1, size - 1)

			# Swap first and second characters
			temp = str_[i]
			str_[i] = str_[ceilIndex]
			str_[ceilIndex] = temp

			# Sort the string on right of 'first char'
			str_ = str_[:i + 1] + sorted(str_[i + 1:])


# Driver program to test above function
str_ = "ABC"
sortedPermutations(str_)

# This code is contributed by phasing17
