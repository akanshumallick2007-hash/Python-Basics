student={
    "name":"akanshu",
    "subjects":{
        "c":56,
        "python":65,
        "html":48
    }
    }
print(len(student),type(student),student)
print(student["name"],student["subjects"])
print("Marks of Python is:",student["subjects"]["python"])

#Methods

print((list(student.keys()))) #return all key
print(list(student.values())) #return all values
print(list(student.items())) #return all key & values in pairs
print(list(student.get("subjects"))) #return key according to value
student.update({"city":"kolkata"}) #insert new items in dictionary
print(student)