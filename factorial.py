no=int(input("enter a number "))
fact=1
for i in range(2,no+1):
    fact=fact*i
print("factorial of {} is {}".format(no,fact))
