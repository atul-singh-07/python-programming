# Q: Creative programme of traffic light simulator where the colour of the light is need to be input where 
#    red=stop, yellow=wait and green=go.

a=input("Enter colour:").lower() # here we used lower function to handle both uppercase and
if(a=="red"):#                     lowercase input of string as lower() convert every input
    print("Stop")#                 in lower case.

elif(a=="yellow"):
    print("Wait")

elif(a=="green"):
    print("Go")

else:
    print("Light is Broken")
    