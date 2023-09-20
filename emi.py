#calculate the emi for amount period and Interest 

p=float(input("enter the principle amount"))
r=float(input("enter the rate of interest"))
t=int(input("enter the time period in MONTHS"))


if(p>0 and t>0 and t<=120 and r>=0 ):
    ir= r/1200
    emi = p * ir * ((1+ir)**t)/((1+ir)**t - 1)
    print(emi)

elif(p<0 and t<0 and r<0):
    print("your principle amount,rate of interest and time period cannot be less than zero")

elif(p<0 and t>=20 and r<0):
    print(" principle amount and rate of interest cannot be less than zero and time period cannot be more than 20 years ")

elif(p<0 and r<0):
    print(" principle amount and rate of interest cannot be less than zero")

elif(p<0 and t>=20):
    print(" principle amount cannot be less than zero and time period cannot be more than 120 months ")


elif(t>=20):
    print("time period cannot be more than 120 months ")

elif(r<0):
    print("the rate of interest cannot be less than zero")

elif(p<0):
    print("principle cannot be zero ")

elif(t<0):
    print("time period cannot be less than zero")

else:
    print("something went wrong, please report the problem ")
    
