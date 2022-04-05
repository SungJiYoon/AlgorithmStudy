N = int(input())
time_list = list(map(int, input().split()))

time_list.sort()
temp = 0
result = 0
for time in time_list:
    temp += time
    result += temp

print(result)