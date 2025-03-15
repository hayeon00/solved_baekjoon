import sys

n = int(sys.stdin.readline())  
rope = [int(sys.stdin.readline()) for _ in range(n)]  

rope.sort() 

max_weight = 0
for i in range(n):
    max_weight = max(max_weight, rope[i] * (n - i))

print(max_weight)