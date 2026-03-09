# List method: are those functions that are only valid to list

a=[2,1,3]
print("Initial list:",a)

a.append(4) # adds the element to the last of list which comes under mutating the list
print("Appending 4:",a)

a.sort() # sorts in ascending order
print("Acending Sorting:",a)

a.sort(reverse=True) # sorts in decending order
print("Decnding Sorting:",a)

a.reverse() # used for reversing complete list
print("Reverse List:",a)

a.insert(4,0) # used for inserting the element to list syntax: list.insert(index,element)
print("After insert:",a)

a.remove(1) # Remove first occurrence of element
print("Remove 1:",a)

a.pop(2) # remove element at index
print("Pop at index 2:",a)

# Note : maximum of these function return None when print(a.sort()) or print(a.append(4)) 
#        because they make direct changes to the initial list


# OUTPUT:
# Initial list: [2, 1, 3]
# Appending 4: [2, 1, 3, 4]
# Acending Sorting: [1, 2, 3, 4]
# Decnding Sorting: [4, 3, 2, 1]
# Reverse List: [1, 2, 3, 4]
# After insert: [1, 2, 3, 4, 0]
# Remove 1: [2, 3, 4, 0]
# Pop at index 2: [2, 3, 0]
