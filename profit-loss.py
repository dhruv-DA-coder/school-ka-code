#calculate profit and loss of a given cost and sell price

x=int(input("enter the price at which you bought the product:"))
y=int(input("enter the price at which you sold the product:"))


if(x>0 and y>0):
    z=x-y
    if(z<0):
        print("you made a profit of", z*-1)
    elif(z==0):
        print("you made no profit :(")
    else:
        print("you lost",z,"rupees")

elif(x<=0 and y<=0):
    print("the price and discount of the product cannot be negative")

elif(x<=0):
    print("the price of the product cannot be less than or equal to 0")

elif(y<=0):
    print("the discount of the product cannot be less than or equal to 0")

else:
    print("something went wrong please report the problem")
