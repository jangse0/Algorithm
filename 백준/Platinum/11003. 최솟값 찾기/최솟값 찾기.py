from collections import deque

N, L = map(int, input().split())
arr = list(map(int, input().split()))

result = []

dq = deque()

for i in range(N):
    if dq and dq[0] < i - L + 1:
        dq.popleft()

    while dq and arr[dq[-1]] > arr[i]:
        dq.pop()

    dq.append(i)
    result.append(arr[dq[0]])

print(*result)
