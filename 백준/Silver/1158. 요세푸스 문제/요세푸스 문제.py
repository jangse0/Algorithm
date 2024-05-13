n, k = map(int, input().split())
result = []

lst = [i for i in range(1, n+1)]
idx = k -1

while lst:
    idx %= len(lst)
    result.append(lst.pop(idx))
    idx += k - 1

print("<", end="")
for i in result[:-1]:
    print(i, end=", ")
print(result[-1], end=">")
