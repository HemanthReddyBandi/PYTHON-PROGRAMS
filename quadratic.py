a,b,c=input("enter the numbers:").split()
a=int(a)
b=int(b)
c=int(c)
root1=0
root2=0
d=(b**2)-4*a*c
root1=(-b + (d**(0.5)))/2*a
root2=(-b - (d**(0.5)))/2*a
print(f"roots:{root1},{root2}")
