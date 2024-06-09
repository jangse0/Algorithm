def min_coins_greedy(n):
    if n in (1, 3):
        return -1
    coins = 0
    while n > 0:
        if n % 5 == 0:
            coins += n // 5
            n = 0
            break
        n -= 2
        coins += 1
        if n < 0:
            return -1
    return coins

n = int(input())
print(min_coins_greedy(n))
