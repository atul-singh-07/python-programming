# Tuple: A built in data type that lets us create immutable sequence of value.

tup=(87,64,33,95,76)
print(type(tup))

# Accessing the Element of tuples using index
print(tup[0])
print(tup[1])

# As tuple is immutable so operation of Updation or making update will result in [ERROR]
# tup[0]=10 ---> error

#              **** Creating Single value or element tuple ****
a=(1,)
print(a)
print(type(a)) 
# note: is we will not use comma(,) then pyhton will consider single element as int datatype