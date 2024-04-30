n=int(input())
l=[]

for i in range(n):
    l.append(int(input()))

for i in range(n-1):
    idx_min=i
    for j in range(i+1, n):
        if l[idx_min]>l[j]:
            idx_min=j
    l[i], l[idx_min]=l[idx_min], l[i]
    print(l[i])
print(l[-1])
