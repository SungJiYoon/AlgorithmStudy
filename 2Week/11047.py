N, K = map(int,input().split())

coins = []
for i in range(N):
    coins.insert(0,int(input()))

result = 0
for coin in coins:
    result += K//coin
    K %= coin

print(result)