#WAP to print the elements of the following list.

num = []
num.append(int(input("1ST NUM:")))
num.append(int(input("2ND NUM:")))
num.append(int(input("3RD NUM:")))
num.append(int(input("4TH NUM:")))
num.append(int(input("5TH NUM:")))
num.append(int(input("6TH NUM:")))
num.append(int(input("7TH NUM:")))
num.append(int(input("8TH NUM:")))
print(type(num),num[0:len(num)])
for i in num:
    print(i)
    i+=1