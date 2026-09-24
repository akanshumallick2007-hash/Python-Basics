marks={}
x=float(input("Enter acc Marks:"))
marks.update({"acc":x})
x=float(input("Enter math Marks:"))
marks.update({"math":x})
x=float(input("Enter comp Marks:"))
marks.update({"comp":x})

print(type(marks),len(marks),marks)