import sys
T = int(sys.stdin.readline().strip())
for _ in range(T):
    L = int(sys.stdin.readline().strip())
    test = [int(x) for x in sys.stdin.readline().split()]
    test.sort(reverse=True)
    result = 0
    for i in range(L-2):
        result = max(result, test[i] - test[i+2])
    print(result)

