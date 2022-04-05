N, M = map(int, input().split())
A = [[0]*M]*N
B = [[0]*M]*N
result = 0

for i in range(N):
    A[i] = list(map(int,input()))

for i in range(N):
    B[i] = list(map(int,input()))

def check(i, j):
    for x in range(i, i+3):
        for y in range(j, j+3):
            if A[x][y] == 0:
                A[x][y] = 1
            else:
                A[x][y] = 0

result = 0
if (N < 3 or M < 3) and A != B:
    result = -1
else:
    for i in range(N-2):
        for j in range(M-2):
            if A[i][j] != B[i][j]:
                result += 1
                check(i, j)

if result != -1:
    if A != B:
        result = -1
print(result)