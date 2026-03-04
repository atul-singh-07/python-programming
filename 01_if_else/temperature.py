# Take temperature in Celsius and print:
# Hot if > 30
# Normal if 15–30
# Cold if < 15

a=float(input("Enter the temperature in celsius :"))
if(a<15):
    print("Cold")
elif(a>=15 and a<=30):
    print("Normal")
else:
    print("Hot")