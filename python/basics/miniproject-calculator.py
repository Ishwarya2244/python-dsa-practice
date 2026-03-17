# MINI_ project ( CALCULATOR)

a=int(input("enter first number:"))
b=int(input("enter second number:"))
op=input("enter operator(+,-,*,/,%):")
if op=="+":
    print(a+b)
elif op=="-":
    print(a-b)
elif op=="*":
    print(a*b)
elif op=="/":
    if b==0:
        print("Division by zero not allowed")
    else:
        print(a/b)
elif op=="%":
    print(a%b)
else:
    print("invalid operator")
