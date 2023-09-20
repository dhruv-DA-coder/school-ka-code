x=int(input("enter the number for which you want tables:"))
y=int(input("enter the starting number from where the tables should start:"))
z=int(input("enter the ending number from where the tables should end:"))

for i in range(y,z+1):
    print(x,"X",i,"=",x*i )
