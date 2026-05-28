# write function to print the element of a list in a single line where list is the parameter 

a=[1,2,3,4,5,6,7,8,9,10]

def same_line(a):
    for i in a:
        print(i,end=" ")# by default in print function end="\n" here we have changed that
    
same_line(a)    