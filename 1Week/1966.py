from collections import deque

TestCase = int(input())

for _ in range(TestCase):
    N, M = map(int,input().split())
    count = 0
    Priority_list = list(map(int, input().split()))
    Priority = []
    for i in range(N):
        Priority.append([])
        Priority[i].append(Priority_list[i])
        if(i==M): Priority[i].append(1)
        else: Priority[i].append(0)

    deq = deque(Priority)
    while len(deq) !=0 :
        value = deq[0][1]
        if(deq[0][0] == max(map(max, deq))):
            deq.popleft()
            count+=1
            if (value == 1): result = count
        else:
            deq.rotate(-1)
    print(result)
