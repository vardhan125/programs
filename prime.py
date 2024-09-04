no=int(input("enter a no"))
if no>1:
    for i in range(2,no):
         if (no%i)==0:
             print(no,"not aprime ")
             break
    else:
        print("prime")
else:
    print("not a prime")







