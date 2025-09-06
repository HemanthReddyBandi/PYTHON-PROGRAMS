a=int(input("give num1:"))
b=int(input("give num2:"))
operator=input("give operator:")
if operator=="+":
    print(a+b)
elif operator=="-":
    print(a-b)
elif operator=="*":
    print(a*b)
elif operator=="%":
    print(a%b)
elif operator=="/":
    print(a/b)
elif operator=="**":
    print(a**b)
else:
    print("operator is not found")