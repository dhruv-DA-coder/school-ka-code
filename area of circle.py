x=float(input("enter the radius of the circle:"))

if(x>=0):
    z=x*3.1415926535897
    print("the area of the circle with radius", x,"is ~",int(z),"or", z)

elif(x<0):
    print("the radius cannot be less than or equal to 0")

else:
    print("something went wrong please report the problem")
