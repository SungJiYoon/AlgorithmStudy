import heapq

N = int(input())
Num_list = [0]*N
for i in range(N):
    Num_list[i] = int(input())

max_heap = []
for item in Num_list:
    if (item == 0) and (len(max_heap) == 0):
        print(0)
    elif item > 0:
        heapq.heappush(max_heap, (-item, item))
    else:
        print(heapq.heappop(max_heap)[1])