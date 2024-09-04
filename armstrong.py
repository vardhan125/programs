no=int(input("enter a no"))
i=no
result=0
n=len(str(no))
while(no!=0):
    digit = no % 10

    result = result +(digit**n)
    no =no // 10


if i == result:
        print("given no is armstrong")
else:
        print("not armstrong")
