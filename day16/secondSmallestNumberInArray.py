# Python prog to illustrate the following in a list
def array_calc(list):
	length = len(list) #this can be later used for finding the largest elements
	list.sort() #we are sorting the list in ascending order
	print("Second Smallest element is:", list[1]) 

# Driver Code
list=[12, 45, 2, 41, 31, 10, 8, 6, 4]
print(list)
result= array_calc(list)
