import sys
n= int(sys.stdin.readline().strip())
sum=0
cnt=0
for i in range(1, n+1):
    if i<(n-sum):
        sum+=i
        cnt+=1
    elif i==(n-sum):
        sum+=i
        cnt+=1
    else:
        break
print(cnt)