# pre-requisite (input integer, lists , variable etc)
x=int(input("enter a number"))
b=int(input("enter another number"))
l=[]
l1=[]
l2=[]
a=1

#checking if the numbers entered are more than zero.
if(x>0 and b>0):

# taking all the divisors of a the first number , adding them to a list and then taking the length of the list.
    for i in range(2,x):
            if (x%i == 0):
                l.append(i)
    y=len(l)
# taking all the divisors of a the second number , adding them to a list and then taking the length of the list.
    for j in range(2,b):
            if (b%j == 0):
                l1.append(j)
    c=len(l1)
# comparing the divisors, if divisors are equal adding it to a list 
    for h in range(0,y):
        for u in range (0,c):
                if(l[h]==l1[u]):
                    l2.append(l[h])
#taking the length list and printing the largest element
    p=len(l2)
    if(p==0):
        print("gcd=1")
    else:
        print("gcd=",l2[p-1])
                    
