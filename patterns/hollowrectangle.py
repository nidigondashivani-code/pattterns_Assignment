m=3
n=5
for i in range(1,m+1):
    for j in range(1,n+1):
        if i==0 or i==n-1 or j==0 or j==m-1:
            print("*",end=" ")

        else:
            print(" ",end=" ")
    print()
