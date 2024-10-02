import sys

n = int(input())
ary = [0] * 10001

for _ in range(n):
    num = int(sys.stdin.readline())
    ary[num] += 1

for i in range(1, 10001):
    if ary[i] > 0:
        for _ in range(ary[i]):
            print(i)