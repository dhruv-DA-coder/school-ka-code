x=float(input("enter the length of the square:"))

if(x>=0):
    z=x*x
    print("the area of the square with length",x,"is",z)

elif(x<0):
    print("the length cannot be less than or equal to 0")

else:
    print("something went wrong please report the problem")
