# Performing slicing operation

# Syntax:list-name[startingindex : endingindex]---> ending index is not included
marks=[86,64,33,95,76]

print(marks[1:4])
print(marks[:4]) #--> [0:4]
print(marks[1:]) #--> [1:len(marks)]
print(marks[-3:-1]) 