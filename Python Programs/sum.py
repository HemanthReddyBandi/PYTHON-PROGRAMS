from numpy import*
str=input('enter a elements for matrix A')
a=reshape(matrix(str),(3,3))
print(a)
print(type(a))
str=input("enter a elements for matrix B")
b=reshape(matrix(str),(3,3))
print(b)
print(type(b))
c=a+b
print ('sum is ::',c)
c=a-b
print ('sub is ::',c)
