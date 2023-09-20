x=int(input("enter the price at which you bought the product:"))
y=int(input("enter the amount of discount:"))


if(x>0 and y>0):
    z=(y/100)*x
    i=x-z
    print("you saved ₹",z,"aand this is the discounted price of the product ₹",i)

elif(x<=0 and y<=0):
    print("the price and discount of the product cannot be negative")

elif(x<=0):
    print("the price of the product cannot be less than or equal to 0")

elif(y<=0):
    print("the discount of the product cannot be less than or equal to 0")

else:
    print("something went wrong please report the problem")
