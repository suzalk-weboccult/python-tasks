n=int(input())

for i in range((2*n)+3):
    for j in range((2*n)+3):
        if j==0 or j==(2*n)+2:
            print("O",end="")
        elif (i==0 and j!=0) or (i==(2*n)+2 and j!=0):
            print("0",end="")
        elif i==n+1 and j==n+1:
            print("O",end="")
        elif i<((2*n)+2)/2 and j<((2*n)+2)/2 and i<j+1:
            print(n-j+1,end="")
        elif i<((2*n)+2)/2 and j>((2*n)+2)/2 and i+j>((2*n)+1):
            print((2*n)+2-j,end="")
        elif i>((2*n)+2)/2 and j<((2*n)+2)/2 and i+j<((2*n)+3):
            print(j,end="")
        elif i>((2*n)+2)/2 and j>((2*n)+2)/2 and i+1>j: 
            print(j-n-1,end="")
        else:
            print(" ",end="")
    print()