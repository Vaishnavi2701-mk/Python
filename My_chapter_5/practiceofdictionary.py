#dictionary
a={"Vaishnavi":"Daughter",
    "Gayatri":"sister",
    "Ajay":"Father",
    "Sushama":"Mother",
    "Mayi":"Grandmother",
    "Numbers":{"int":34,"float":43.4,"bool":"true/false"}}
#print(a["Mayi"])   #It will give a value of a key
#print(a["Ajay"])
#a["Gayatri"]="Girl"                       **it will update the value**
#print(a.items())                          **print the key-value pair in the form of list**
#print(a.keys())                           **print the keys in the form of list
#print(a.values())                         ** print the values in the form of list
#print(type(a.values))                     ** it will give a type as "dict_values" but print in the format of list and similar for keys**
#a.update({"Parth":"Brother"})             ** it will update  dictionary by new key value pair  
#print(a)
#print(a["float"])                         ** even though float is a key but it is nested under the key number thus it is consider as value for that**
#print(a["Numbers"]["float"])              ** now it is true
#print(a["Ajay"])                          ** this both gives the same value when key is present
#print(a.get("Ajay"))
# But when key is not avilable then it will do different work
#print(a["Pinki"])                         ** it will give error because key is not present
print(a.get("Pinki"))                     #** It will show none
