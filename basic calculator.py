x=int(input("enter the first number:"))
y=int(input("enter the second number:"))
z=input("enter the operator:")

if(z=="+"):
    print ("the sum of ",x,"and",y, "is equal to", x+y)
elif(z=="-"):
    print ("the difference of ",x,"and",y, "is equal to", x-y)
elif(z=="*"):
    print ("the product of ",x,"and",y, "is equal to", x*y)
elif(z=="/"):
    if(y==0):
        print("division by zero is not possible")
    else:
        print ("the quotient of ",x,"and",y, "is equal to", x/y)
else:
    print("enter the correct operator. ")
