# Creating Sets
myset = {1, 2} # Directly assigining values to a set
myset = set() # initializing a set
myset = set(['a', 'b']) # Creating a set
print("myset is ", myset, "\n")

# Modifying Sets
myset.add('c')
print("myset after adding c ", myset, "\n")
myset.add((5,4))
print("myset after adding tuple ", myset, "\n")

myset.update([1,2,3,4])
print("myset is ", myset, "\n")

myset.update({1,7,8})
print("myset is ", myset, "\n")

myset.update({1,6}, [5,13])
print("myset is ", myset, "\n")

myset.update((20,21))
print("myset is ", myset, "\n")

# Removing Items
# If value is not present, discard() does nothing, but remove() will raise a KeyError exception
myset.discard(10)
myset.remove(13)

print("myset is ", myset, "\n")
