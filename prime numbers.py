a=int(input("enter the starting number :"))
b=int(input("enter the ending number :"))

if(a>1 and b>a):
    for x in range(a,b+1):
        for i in range(2,x):
            if (x%i == 0):
                print(x,"not a prime number")
                break
        else:
            print (x,"is a prime number")
else:
    print(" the starting number should be less than ending number and starting number has to be more than zero")


