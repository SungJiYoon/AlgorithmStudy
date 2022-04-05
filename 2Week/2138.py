N = int(input())
old_light = [0]*N
current_light = [0]*N

old_light = list(map(int, input()))
current_light = list(map(int, input()))

def change(num):
    if num == 0:
        num = 1
    else:
        num = 0
    return num

def switch(old_light, cnt):
    count = cnt
    if count == 1:
        old_light[0] = change(old_light[0])
        old_light[1] = change(old_light[1])
    for i in range(1, N):
        if old_light[i-1] != current_light[i-1]:
            count += 1
            old_light[i-1] = change(old_light[i-1])
            old_light[i] = change(old_light[i])
            if i != N-1:
                old_light[i+1] = change(old_light[i+1])
    if old_light == current_light:
        return count
    else:
        return -1

res1 = switch(old_light[:], 0)
res2 = switch(old_light[:], 1)
if res1 >= 0 and res2 >= 0:
    print(min(res1, res2))
elif res1>=0 and res2 < 0:
    print(res1)
elif res1 <0 and res2 >= 0:
    print(res2)
else:
    print(-1)
