n,x=map(int,input().split())
tmp=list(map(int,input().split()))
for i in range(n):
    if(tmp[i]<x):
        print(tmp[i], end=" ")