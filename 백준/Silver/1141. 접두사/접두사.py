n=int(input())
lst=[]
cnt=0

for _ in range(n):
    lst.append(input())

lst.sort(key=len)

for i in range(n):
    a=True
    for j in range(i+1, n):
        if lst[i]==lst[j][:len(lst[i])]:
            a=False
    if a:
        cnt+=1

print(cnt)