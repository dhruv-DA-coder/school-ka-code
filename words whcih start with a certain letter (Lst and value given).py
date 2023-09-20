L= ["Akash", "Nikhil", "Manjeet", "akshat"]
Li=[] 
y= "A"

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

