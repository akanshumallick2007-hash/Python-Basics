age=int(input("Enter your Age: "))
if(age<18):
    print("You cannot vote and not applicable for licence")
elif(age>=90):
    print("You can vote but you now you are not applicable for licence")
else:
    print("You can vote and applicable for licence")