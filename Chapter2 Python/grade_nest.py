#nesting
mark=float(input("Enter your Marks(0-100):"))
if(mark>=0 and mark<=100):
    if(mark>=90):
        print("A+")
    elif(mark>=80):
        print("A")
    elif(mark>=70):
        print("B+")
    elif(mark>=60):
        print("B")
    elif(mark>=50):
        print("C")
    else:
        print("Failed")
else:
    print("Please enter the valid Number")