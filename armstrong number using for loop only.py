num=input("enter a number:")

jum=0
sum=0
l=[]
if(num):
    for i in num:
        if(i=="1"):
            j=1**3
            sum=+j
        elif(i=="2"):
            j=2**3
            sum=+j
        elif(i=="3"):
            j=3**3
            sum=+j
        elif(i=="4"):
            j=4**3
            sum=+j
        elif(i=="5"):
            j=5**3
            sum=+j
        elif(i=="6"):
            j=6**3
            sum=+j
        elif(i=="7"):
            j=7**3
            sum=+j
        elif(i=="8"):
            j=8**3
            sum=+j
        elif(i=="9"):
            j=9**3
            sum=+j
        elif(i=="0"):
            j=0
            sum=+j
        jum=jum+sum
        a= int(num)
if(a==jum):
    print(num, "is a armstrong number")
else:
    print(num, "is not a armstring number")
