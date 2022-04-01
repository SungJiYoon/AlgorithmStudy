import heapq

N = int(input())
num_list = [0]*N
for i in range(N):
    num_list[i] = int(input())

min_heap = []
for item in num_list:
    if (item == 0) and (len(min_heap) == 0):
        print(0)
    elif item != 0:
        heapq.heappush(min_heap, (abs(item), item))
    else:
        print(heapq.heappop(min_heap)[1])