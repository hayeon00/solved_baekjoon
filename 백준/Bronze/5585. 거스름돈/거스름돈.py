n=int(input())

na=1000-n;
cnt=0
while na!=0:
    if na>=500:
        cnt+=na//500
        na=na%500
    elif na>=100:
        cnt+=na//100
        na=na%100
    elif na>=50:
        cnt+=na//50
        na=na%50
    elif na>=10:
        cnt+=na//10
        na=na%10
    elif na>=5:
        cnt+=na//5
        na=na%5
    elif na>=1:
        cnt+=na//1
        na=na%1
    
print(cnt)




    


