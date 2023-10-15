# factorial

n=int(input("enter a number:"))
f=1
if(n<0):
    print("factorial does not exist")
elif(n==0):
    print("facctorial of 0 is 1")
else:
    for i in range (1, n+1):
        f*=i
    print("the factorial of",n ,"is ",f)
