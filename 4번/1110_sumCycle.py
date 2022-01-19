n=int(input())
org=n
count=0
while True:
    a=n//10
    b=n%10
    tmp=(a+b)%10
    n=b*10+tmp
    count+=1
    if org==n:
        break
print(count)
