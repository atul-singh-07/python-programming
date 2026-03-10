dict={
    "name":"Atul",
    "Age":19,
    "Dob":[7,10,2006],
    "Subject":("C","Pyhton","Arduino","Esp32"),
}

print(dict.keys()) # for printing all the keys of a dictionary
print(dict.values()) # return all the values of a dictionary
print(dict.items()) # return all the key:value pair of a dictionary

print(dict.get("name")) 
#  note: work same as dict[name] but with a small difference that if the key is not present
#        in the dictionary then dict[name2] will give---> ERROR
#        whereas dict.get(name2) will return---> NONE


# updating the dictionary
dict.update({"city":"Delhi"})

print(dict)