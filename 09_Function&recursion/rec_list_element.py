# write recursive function to print all elements in a list Hint use list and index as parameter.

a=[1,2,3,4,5,6,7,8]

def print_list(a,index):
    if(index==len(a)):
        return
    print(a[index])
    print_list(a,index+1)

print_list(a,0)