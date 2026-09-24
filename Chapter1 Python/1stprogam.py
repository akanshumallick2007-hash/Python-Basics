#without datatypes
name= input("Enter your Name:")
age= input("Enter your Age:")
marks= input("Enter your Marks:")

print("Welcome",name)
print("Your Age is:",type(age),age)
print(type(marks),marks) #to show the datatypes

#with datatypes
place= str(input("Where do You Live:"))
pincode= int(input("What is your Pincode is:"))
scgp= float(input("What is SCGP:"))

print("You Live in:",place)
print("Pincode is:",pincode)
print(type(scgp),scgp)