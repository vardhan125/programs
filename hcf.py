no1=int(input("enter a number "))
no2=int(input("ener a number "))
m=1
for i in range(1,no1+1):
    if no1%i==0 and no2%i==0 :
        m=i
        print("hcf of{} and {} is {}".format(no1,no2,m))
