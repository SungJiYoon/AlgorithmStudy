N = int(input())
old_light = [0]*N
current_light = [0]*N

old_light = list(map(int, input()))
current_light = list(map(int, input()))

result = 0

def light(i):
    if i != 0 and i != (N-1):
        for x in range(i - 1, i + 2):
            if old_light[x] == 0:
                old_light[x] = 1
            else:
                old_light[x] = 0
    else:
        if old_light[i] == 0:
            old_light[i] = 1
        else:
            old_light[i] = 0
        if i == 0:
            if old_light[i - 1] == 0:
                old_light[i - 1] = 1
            else:
                old_light[i - 1] = 0
        elif i == N-1:
            if old_light[i + 1] == 0:
                old_light[i + 1] = 1
            else:
                old_light[i + 1] = 0

if old_light == current_light:
    print(result)
else:
    while old_light != current_light:
        for i in range(N):
            if current_light[i] == 1:
                light(i)
                result += 1
                break
        if current_light == [0,0,0]:
            result = -1
            break
    print(result)

