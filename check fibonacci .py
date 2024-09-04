import math
def perfectsqure(x):
    s=int(math.sqrt(x))
    return  s*s==x
n=int(input("enter the number"))
res1=5*(n*n)+4
res2=5*(n*n)-4

if perfectsqure(res1) or perfectsqure(res2):
    print(n,"is a fibonacci number ")
else:
    print(n,"not a fibonacci number")
