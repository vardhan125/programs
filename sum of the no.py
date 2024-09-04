n=int(input("enter the positive integer"))
result=0
while n>0:
    digit=n%10
    result=result*10+digit
    n=n//10
print("sum is",result)