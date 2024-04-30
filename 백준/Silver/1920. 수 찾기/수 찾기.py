import sys

n=int(sys.stdin.readline().strip())
a=list(map(int, sys.stdin.readline().split()))
a.sort()
m=int(sys.stdin.readline().strip())
l=list(map(int, sys.stdin.readline().split()))
    
for i in l:
    first, last = 0, n - 1
    while first <= last:
        mid = (first + last) // 2
        if a[mid] == i:
            print(1)
            break
        if a[mid] > i:
            last = mid - 1
            continue
        else:
            first = mid + 1
            continue
    else:    
        print(0)