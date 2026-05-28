subject={}# empty dictionary

x=int(input("Enter marks of physics:"))
y=int(input("Enter marks of chemistry:"))
z=int(input("Enter marks of maths:"))

subject.update({"physics":x})
subject.update({"chemistry":y})
subject.update({"math":z})

print(subject)