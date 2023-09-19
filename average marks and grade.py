a=int(input("enter your english marks out of 100:"))
b=int(input("enter your mathematics marks out of 100:"))
c=int(input("enter your physics marks out of 100:"))
d=int(input("enter your chemistry marks out of 100:"))
e=int(input("enter your artificial intellegence marks out of 100:"))
f=int(input("enter your informatics practices marks out of 100:"))

if(a>0 and b>0 and c>0 and d>0 and e>0 and f>0 and a<100 and b<100 and c<100 and d<100 and e<100 and f<100):
    x=(a+b+c+d+e+f)/6

    if(x>=95):
        print("potencial valedictorian")

    elif(x>=90):
        print("great job you passed with A grade")
        print("your average would be",x)

    elif(x>=80 and x<90):
        print("keep up the work you passed with B grade")
        print("your average would be",x)

    elif(x>=70 and x<80):
        print("you survived and passed with C grade")
        print("your average would be",x)

    elif(x>=60 and x<70):
        print("you survived and passed with C grade")
        print("your average would be",x)

    elif(x<60):
        print("bro u failed + ratio")
        print("your average would be",x)

    else:
        print("bruh")

elif(a<0 and b<0 and c<0 and d<0 and e<0 and f<0):
    print("enter positive values less than 100 for your marks")

elif(a>100 and b>100 and c>100 and d>100 and e>100 and f>100):
    print("enter values less than 100 for your marks")


elif(a<0):
    print("enter positive marks for english marks")

elif(a>100):
    print("enter marks less than 100 for english")


elif(b<0):
    print("enter positive marks for mathematics marks")

elif(b>100):
    print("enter marks less than 100 for mathematics")


elif(c<0):
    print("enter positive marks for physics marks")

elif(c>100):
    print("enter marks less than 100 for physics")


elif(d<0):
    print("enter positive marks for chemistry marks")

elif(d>100):
    print("enter marks less than 100 for chemistry")


elif(e<0):
    print("enter positive marks for articial intellegence marks")

elif(e>100):
    print("enter marks less than 100 for artificail intellegence")
    
    
elif(f<0):
    print("enter positive marks for informatics practices marks")

elif(f>100):
    print("enter marks less than 100 for informatics practices")
