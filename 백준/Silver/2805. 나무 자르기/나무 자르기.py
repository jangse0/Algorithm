import sys

n, m=map(int, sys.stdin.readline().split())
tree=list(map(int, sys.stdin.readline().split()))
first, last = 0, max(tree)

while first<=last:
    mid = (first + last)//2
    m_l=0
    m_l = sum(t - mid for t in tree if t > mid)
    if m_l>=m:
        first = mid+1
    else:
        last=mid-1

print(last)
