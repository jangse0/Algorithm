import sys
import collections

n = int(input())
numbers = [int(sys.stdin.readline()) for _ in range(n)]

mean = round(sum(numbers) / n)

numbers.sort()
median = numbers[n // 2]

count = collections.Counter(numbers)
most_common = count.most_common()
most_common.sort(key=lambda x: (-x[1], x[0]))

if n > 1 and most_common[0][1] == most_common[1][1]:
    mode = most_common[1][0]
else:
    mode = most_common[0][0]

_range = numbers[-1] - numbers[0]

print(mean)
print(median)
print(mode)
print(_range)
