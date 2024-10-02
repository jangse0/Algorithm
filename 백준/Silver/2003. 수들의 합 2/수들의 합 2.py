n, m = map(int,input().split())
l=list(map(int,input().split()))

left = 0
right = 1
cnt = 0
s=l[0]

while True:
    if s < m:
        if right < n:
            s += l[right]
            right += 1
        else:
            break
    elif s == m:
        cnt += 1
        s -= l[left]
        left += 1
    else:
        s -= l[left]
        left += 1

print(cnt)