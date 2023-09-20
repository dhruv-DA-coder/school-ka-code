x=float(input("enter the length of the rectangle:"))
y=float(input("enter the breadth of the rectangle:"))


if(x>0 and y>0):
    z=x*y
    print("the area of the rectangle with length",x, "and breadth",y, "is",z)

elif(x<=0 and y<=0):
    print("the length and breadth cannot be less than or equal to 0")

elif(x<=0):
    print("the length cannot be less than or equal to 0")

elif(y<=0):
    print("the breadth cannot be less than or equal to 0")

else:
    print("something went wrong please report the problem")
