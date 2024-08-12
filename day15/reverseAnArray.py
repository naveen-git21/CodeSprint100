
# Reversing a list using slicing technique
def Reverse(lst):
   new_lst = lst[::-1]
   return new_lst


lst = [10, 11, 12, 13, 14, 15]
print(f"Original array {lst}")
print(f"Reversed array {Reverse(lst)}")

"""
lst = [10, 11, 12, 13, 14, 15]
lst.reverse()
print("Using reverse() ", lst)

print("Using reversed() ", list(reversed(lst)))


"""