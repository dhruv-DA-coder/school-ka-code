x=float(input("enter the height of the triangle:"))
y=float(input("enter the base of the triangle:"))


if(x>0 and y>0):
    z=(x*y)/2
    print("the area of the triangle with height",x, "and base",y, "is",z)

elif(x<=0 and y<=0):
    print("the height and base cannot be less than or equal to 0")

elif(x<=0):
    print("the height cannot be less than or equal to 0")

elif(y<=0):
    print("the base cannot be less than or equal to 0")

else:
    print("something went wrong please report the problem")
