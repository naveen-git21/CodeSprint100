array=[45, 36 ,35 ,25,79,89,70,11]
array1=array
print(f"The original array is {array}")
array.sort()
#sorted_array=sorted(array) 
# #this method can also be used to sort array and you can save it in a new variable
print(f"Sorted array in ascending order is {array}")

array1.sort(reverse=True)
#sorted_array1=sorted(array1,reverse=True) 
print(f"Sorted array in descending order is {array1}")

