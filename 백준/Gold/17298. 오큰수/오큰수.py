import sys

n = int(sys.stdin.readline())
m = list(map(int, sys.stdin.readline().split()))
stack = []
ans = [-1 for _ in range(n)]

for i in range(n):
    while stack and m[stack[-1]] < m[i]:
        ans[stack.pop()] = m[i]
    stack.append(i)
    
print(*ans)