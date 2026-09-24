#WAP to search for a number x in tuple.

num=(1,4,9,16,25,36,49,64,81,100,4)
print(num[0:len(num)])
j=int(input("Enter your Number:"))
for i in num:
    if(i==j):
        print("Found",i)
    else:
        print("Finding",i)
    i+=1
