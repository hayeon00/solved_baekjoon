n=int(input())

a=list(map(int,input().split()))
b=list(map(int,input().split()))

a.sort()

sorted_indices=sorted(range(n),key=lambda i:-b[i])
new_a=[0]*n
for i in range(n):
    new_a[sorted_indices[i]] = a[i]

total_sum=sum(new_a[i]*b[i] for i in range(n))
print(total_sum)