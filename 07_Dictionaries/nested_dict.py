student={
    "Name":"Atul",
    "Score":{
        "Phy":98,
        "Chem":97,
        "Math":35
    }
}

print(student)

# Accessing the key value in nested dictionaries

print(student["Name"])
print(student["Score"])

print("Printing the score of physics:",student["Score"]["Phy"])