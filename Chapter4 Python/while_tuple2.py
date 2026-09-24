#WAP to search for a number X in this tuple using loop.

#num=(1,4,9,16,25,36,49,64,81,100,36)
num=[]
num.append(int(input("1ST NUM:")))
num.append(int(input("2ND NUM:")))
num.append(int(input("3RD NUM:")))
num.append(int(input("4TH NUM:")))
num.append(int(input("5TH NUM:")))
num.append(int(input("6TH NUM:")))
num.append(int(input("7TH NUM:")))
num.append(int(input("8TH NUM:")))
print(type(num),num[0:len(num)])

x=int(input("Enter the Number you want to find:"))
i=0
while i<len(num):
    if(num[i] == x):
        print("Found",num[i])
    else:
        print("Finding",num[i])
    i+=1