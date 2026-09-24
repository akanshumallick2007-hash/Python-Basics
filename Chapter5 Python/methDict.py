student={
    "name":"akanshu",
    "subjects":{
        "math":56,
        "html":45,
        "dbms":40
    }
}
print(student)
print(student["subjects"])
print(len(student))

#Methods

print(list(student.keys())) #return all key
print(list(student.values())) #return all values
print(list(student.items())) #return all key & values in pairs
print(list(student.get("subjects"))) #return key according to value
(student.update({"city":"Kolkata"})) #insert new items in dictionary
print(student)