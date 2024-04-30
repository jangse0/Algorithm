n=int(input())
cnt=0

if n>=100:
    cnt+=99
    for i in range(100, n+1):
        n_l=list(map(int, str(i)))
        if n_l[0]-n_l[1]==n_l[1]-n_l[2]:
            cnt+=1
else:
    cnt=n

print(cnt)