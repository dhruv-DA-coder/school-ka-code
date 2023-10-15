# getting a integer input from the user 

x=int(input("enter a number:"))

# checking if the number is divisible by both the 3 and 5

if(x%3==0 and x%5==0):
    print("Fizzbuzz")

 #checking if number is divisible by 3 or 5
 
else:
    if(x%3==0):
        print("fizz")
    elif(x%5==0):
        print("buzz")
    else:
        print("No fizzbuzz")
