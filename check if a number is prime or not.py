x=int(input("enter the starting number :"))

if(x>0):
    for i in range(2,x):
        if (x%i == 0):
            print(x,"not a prime number")
            break
        else:
            print (x,"is a prime number")
else):
    print("")
