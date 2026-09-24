#WAP to check if a list contains a palindrome of elements

num=[]
num.append(int(input("Enter 1st Num:")))
num.append(int(input("Enter 2nd Num:")))
num.append(int(input("Enter 3rd Num:")))
print(type(num),num)
num_copy=num.copy()
num_copy.reverse()
if(num_copy==num):
    print("It's a Palindrome Number")
else:
    print("It's not a Palindrome Number")