L=int(input())
st=input()
a='a'
result=0

for i in range(L):
    tmp=(ord(st[i])-ord(a))+1
    result+=tmp*(31**i)


print(result)