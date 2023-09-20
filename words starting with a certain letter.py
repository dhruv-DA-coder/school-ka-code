x=int(input ("enter the number of values you will be adding to the list:"))
y=str(input(" enter the letter which the words should start from"))
L=[]
Q=[]
Li=[]

for j in y:
    Q.append(j)
    z=len(Q)
if (z==1):
    for i in range(1,x+1):
        a=str(input("enter the words "))
        n=a
        L.append(n)
        m=len(L)
    for i in range (0, m):
        Li.append(L[i])
        for j in L[i]:
            if(j==y):
                print("the word",Li, " does start with",y)
                break
            else:
                print("the word",Li, " does not start with",y)
                break
        Li.clear()
else:
    print("please enter only one letter for the second value") 

