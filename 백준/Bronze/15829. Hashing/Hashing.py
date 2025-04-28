#Hashing

#해시함수?
#입력으로 들어올 수 있는 문자열 종류는 무한하지만 출력범위는 정해져있도록 만드는 함수

#문자열을 숫자로 매핑(a는 1,b는 2 ..)
# 각항에 해당하는 특정 숫자를 곱합?
# r=31
# M=1234567891로 주어짐

L=int(input())
st=input()
a='a'
result=0
r=31
M=1234567891


for i in range(L):
    tmp=(ord(st[i])-ord(a))+1
    result+=tmp*(r**i)

result%=M

print(result)


    


