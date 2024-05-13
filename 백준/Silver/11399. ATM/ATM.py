def solve(n):
    arr=list(map(int, input().split()))
    arr.sort()
    for i in range(1, n):
        arr[i]+=arr[i-1]
    print(sum(arr))
    
n=int(input())
solve(n)