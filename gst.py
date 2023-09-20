x=float(input("enter price of product in rupees with out tax:"))

if(x>0):
    y=x*0.18
    print("your income tax is ",y)

else:
    print("your income cannot be less than or equal to zero")
