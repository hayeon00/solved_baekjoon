n=int(input())

for _ in range(n):
    reversed_s=[]
    s=list(input().split())

    for word in s:
        reversed_s.append(''.join(reversed(word)))
    print(' '.join(reversed_s))



