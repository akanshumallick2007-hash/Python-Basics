#WAP to search for a number X in this tuple using loop.

num=(1,4,9,16,25,36,49,64,81,100,36)
print(num[0:len(num)]) 
#traverse
x=36
i=0
while i<len(num):
    if(num[i] == x):
        print("Found",num[i])
    else:
        print("Finding",num[i])
    i+=1