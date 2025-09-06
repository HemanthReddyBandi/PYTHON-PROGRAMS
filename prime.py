n=int(input("enter a number:"))
for j in range(n+1):
    for i in range(2,j):
        if j%i==0:
            break
        else:
            
            print(j)
    