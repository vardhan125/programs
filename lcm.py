def compute_lcm(n1, n2,):
    if n1>n2:
        higher = n1
    else:
        higher= n2
        value=higher
    while True:
        if higher%n1==0 and higher%n2==0:
            print("the lcm of ",n1, "and",n2, "is",higher)
            break
        else:
            higher=higher+value

n1=int(input("enter the firstno"))
n2=int(input("enter the second no"))
compute_lcm(n1,n2)

