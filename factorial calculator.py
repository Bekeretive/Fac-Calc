#Asking the user to enter number for which he wants to find the factorial
number = int(input("Enter the Number: "))

factorial = 1

if ( number < 0 ):
    print ("Sorry We Can't Compute Negative Numbers")
elif ( number < 2):
    print("{}! = {}".format(number,factorial))
else:
    for num in range(number,1 , -1):
        factorial = factorial * num
print("{}! = {}".format(number,factorial))