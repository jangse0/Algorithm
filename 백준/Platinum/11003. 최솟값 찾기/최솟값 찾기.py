from collections import deque

# 데이터 입력
N, L = map(int, input().split())
arr = list(map(int, input().split()))

# 결과를 저장할 리스트
result = []

# 최소값을 유지할 덱 선언
dq = deque()

for i in range(N):
    # 덱의 첫 번째 원소가 윈도우 범위를 벗어나면 제거
    if dq and dq[0] < i - L + 1:
        dq.popleft()

    # 덱에 있는 값이 현재 arr[i]보다 크면 제거 (최소값을 유지하기 위함)
    while dq and arr[dq[-1]] > arr[i]:
        dq.pop()
    
    # 현재 인덱스를 덱에 추가
    dq.append(i)
    
    # 덱의 첫 번째 원소가 윈도우의 최소값
    result.append(arr[dq[0]])

# 결과 출력
print(*result)
