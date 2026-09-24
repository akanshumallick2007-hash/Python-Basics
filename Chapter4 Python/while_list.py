# WAP to print the elemnts of the following list using a loop.

"""num=[1,4,9,16,25,36,49,64,81,100]"""
num=[]
num.append(int(input("1ST NUM:")))
num.append(int(input("2ND NUM:")))
num.append(int(input("3RD NUM:")))
num.append(int(input("4TH NUM:")))
num.append(int(input("5TH NUM:")))
num.append(int(input("6TH NUM:")))
num.append(int(input("7TH NUM:")))
num.append(int(input("8TH NUM:")))
print(num[0:len(num)]) 
#traverse
i=0
while i<len(num):
    print(num[i])
    i+=1