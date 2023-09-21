x=int(input("enter the starting number :"))

if(x>2):
    for i in range(2,x):
        if (x%i == 0):
            print(x,"not a prime number")
            break
        else:
            print (x,"is a prime number")
elif(x==2):
    print(x,"is a prime")

else:
    print(x,is not a prime)