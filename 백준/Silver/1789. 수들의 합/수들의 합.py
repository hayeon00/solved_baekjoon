s=int(input())
n=1
sum=0

while True:
    if s-sum<n:
        n-=1
        break
    sum+=n
    n+=1

print(n)