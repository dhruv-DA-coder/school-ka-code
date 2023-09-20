x=float(input("enter a your annual income in rupees:"))

if(x>0 and x<300000):
    a=x*0
    print("your income tax is ",a)

elif(x>300000 and x<600000):
    b=x*0.05
    print("your income tax is",b)

elif(x>600000 and x<900000):
    c=x*0.10
    print ("you income tax is", c)

elif(x>900000 and x<1200000):
    d=x*0.15
    print ("you income tax is" ,d)

elif(x>1200000 and x<1500000):
    e=x*0.20
    print ("you income tax is" ,e)

elif( x>1500000):
    f=x*0.3
    print ("you income tax is" ,f)

else:
    print("your income cannot be less than or equal to zero")
