#programm for binomial coefficient.

n=int(input("enter the value for n :"))
r=int(input("enter the value for r :"))

j=n-r
f=1
g=1
h=1

#factorials of n , r and n-c.

if(r<=n and n>0 and r>0):
    for i in range (1, n+1):
        f*=i
    for i in range (1, r+1):
        g*=i
    for i in range (1, j+1):
        h*=i
#insering values of n ,r and n-c in the formula
    x=f/(g*h)

    print("the binomial coefficient with n=",n,"and r=",r,"is",x)
else:
    print("error :The values should follow these rules r<=n and n>0 and r>0.")
