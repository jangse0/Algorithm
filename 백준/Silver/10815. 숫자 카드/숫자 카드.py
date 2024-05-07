n=int(input())
n_l=list(map(int, input().split()))
n_l.sort()
m=int(input())
m_l=list(map(int, input().split()))
p=[]

for i in m_l:
    first, last=0, n-1
    while first<=last:
        mid=(first+last)//2
        if n_l[mid] == i:
            p.append(1)
            break
        if n_l[mid]>i:
            last = mid - 1
            continue
        else:
            first=mid + 1
            continue
    else:
        p.append(0)

print(*p)