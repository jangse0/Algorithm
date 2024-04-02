n, m = map(int, input().split())
matrix = []
cnt = []

for i in range(n):
    matrix.append(input())

for i in range(n - 7):
    for j in range(m - 7):
        c_w = 0
        c_b = 0
        for k in range(i, i + 8):
            for l in range(j, j + 8):
                if (k + l) % 2 == 0:
                    if matrix[k][l] != 'W':
                        c_w += 1
                    else:
                        c_b += 1
                else:
                    if matrix[k][l] != 'W':
                        c_b += 1
                    else:
                        c_w += 1
        cnt.append(min(c_w, c_b))

print(min(cnt))