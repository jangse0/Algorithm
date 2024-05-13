lst=[i for i in range(1, 10001)]
s=set()

for i in range(1, 10001):
    for j in str(i):
        i+=int(j)
    s.add(i)

print(*sorted((set(lst)-s)))