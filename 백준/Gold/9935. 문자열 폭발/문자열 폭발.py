import sys

st=list(sys.stdin.readline().strip())
remove_st=list(sys.stdin.readline().strip())

ln=len(remove_st)
stack=[]

for i in st:
    stack.append(i)
    if stack[len(stack)-ln:len(stack)]==remove_st:
        for _ in range(ln):
            stack.pop()

if stack:
    print(*stack, sep='')
else :  
    print("FRULA")