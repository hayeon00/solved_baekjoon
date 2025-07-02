from collections import deque

n=int(input())

for i in range(n):
    op=input()
    n=int(input())
    s=input()
    s=s.strip('[]')
    if s:
        arr = deque(map(int, s.split(',')))
    else:
        arr=deque()

    reverse_flag = False
    err_flag = False

    for cmd in op:
        if cmd=='R':
            reverse_flag=not reverse_flag
        elif cmd=='D':
            if arr:
                if reverse_flag:
                    arr.pop()
                else:
                    arr.popleft()
            else:
                print("error")
                err_flag=True
                break

    if not err_flag:
        if reverse_flag:
            arr.reverse()
        print("[" + ",".join(map(str, arr)) + "]")





