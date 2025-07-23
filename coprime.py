from math import gcd
num1=int(input("number1"))
num2=int(input("number2"))
if gcd(num1,num2)==1:
    print("coprime numbers")
else:
    print("not coprime number")
