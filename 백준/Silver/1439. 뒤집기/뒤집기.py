st=input()

cnt_0=0
cnt_1=0

for i in range(1,len(st)):
    if st[i-1]=='0' and st[i]=='1':
        cnt_0+=1
    elif st[i-1]=='1' and st[i]=='0':
        cnt_1+=1

if st[len(st)-1]=='0':
    cnt_0+=1
else:
    cnt_1+=1


print(min(cnt_0,cnt_1))

# 0->1이면 카운트0, 1->0이면 카운트1
# 마지막이 0이면 카운트0, 마지막이 1이면 카운트1