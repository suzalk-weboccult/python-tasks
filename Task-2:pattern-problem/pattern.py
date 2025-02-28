n=int(input())
num=n
count = len(str(n))

for i in range((2*n)+3):
    for j in range((2*n)+3):
        if j==0 or j==(2*n)+2:
            print(count*"O",end="")
        elif (i==0 and j!=0) or (i==(2*n)+2 and j!=0):
            print(count*"0",end="")
        elif i==n+1 and j==n+1:
            print(count*"O",end="")
        elif i<((2*n)+2)/2 and j<((2*n)+2)/2 and i<j+1:
            print(f"{n-j+1:{count}}",end="")
        elif i<((2*n)+2)/2 and j>((2*n)+2)/2 and i+j>((2*n)+1):
            print(f"{((2*n)+2-j):{count}}",end="")
        elif i>((2*n)+2)/2 and j<((2*n)+2)/2 and i+j<((2*n)+3):
            print(f"{j:{count}}",end="")
        elif i>((2*n)+2)/2 and j>((2*n)+2)/2 and i+1>j: 
            print(f"{j-n-1:{count}}",end="")
        else:
            print(count*" ",end="")
    print()