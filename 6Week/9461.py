n = int(input())
memo = [0 for _ in range(101)]
for i in range(0, 4):
    memo[i] = 1
for j in range(4, 6):
    memo[j] = 2
for _ in range(n):
    m = int(input())
    for k in range(6, m+1):
        memo[k] = memo[k-1] + memo[k-5]

    print(memo[m])
