def CommonSubsequencesCount(s, t):
	n1 = len(s)
	n2 = len(t)

	# to store previous computations of subproblems
	prev = [0] * (n2 + 1)

	# for each character of S
	for i in range(1, n1 + 1):
		curr = [0] * (n2 + 1)
		# for each character in T
		for j in range(1, n2 + 1):
			# if characters are the same in both strings
			if s[i - 1] == t[j - 1]:
				curr[j] = 1 + curr[j - 1] + prev[j]
			else:
				curr[j] = curr[j - 1] + prev[j] - prev[j - 1]
		# assigning values for iteration
		prev = curr
	
	# return the final answer
	return prev[n2]

# Driver Program
if __name__ == "__main__":
	s = "ajblqcpdz"
	t = "aefcnbtdi"
	print(CommonSubsequencesCount(s, t))
