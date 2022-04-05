from sys import stdin

N = int(stdin.readline())

rooms = [0]*N
for i in range(N):
    rooms[i] = tuple(map(int,stdin.readline().split()))

rooms.sort(key=lambda x:x[0])
rooms.sort(key=lambda x:x[1])

result = 1
last = rooms[0][1]
for i in range(1,N):
    if last <= rooms[i][0]:
        result += 1
        last = rooms[i][1]

print(result)