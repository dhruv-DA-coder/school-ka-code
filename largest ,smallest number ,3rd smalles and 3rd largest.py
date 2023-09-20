x=int(input ("enter the number of values you will be adding to the list:"))
L=[]
for i in range(1,x+1):
    a=int(input("enter the values for "))
    n=a
    L.append(n)
L.sort()
print ("the smallest number in the list is", L[0])
print ("the largest number in the list is", L[x-1])

print ("the 3rd smallest number in the list is", L[2])
print ("the 3rd largest number in the list is", L[x-3])
