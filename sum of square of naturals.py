n=int(input("enter a number:"))

x=0

if(n>1):
    for i in range(1,n+1):
        s=i**2
        x+=s
    print(x)

else:
    print(n, "is not a natural number")
