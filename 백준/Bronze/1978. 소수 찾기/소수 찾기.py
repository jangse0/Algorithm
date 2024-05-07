n=int(input())
l=list(map(int,input().split()))
cnt=n

for i in range(len(l)):
    if l[i]==1:
        cnt-=1
        continue
    if l[i]==2:
        continue
    for j in range(2, l[i]):
        if l[i]%j==0:
            cnt-=1
            break

print(cnt) 