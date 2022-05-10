import sys

n = int(sys.stdin.readline())
budget = list(map(int, sys.stdin.readline().split()))
m = int(sys.stdin.readline())

_max = max(budget)
_min = 1

while _max >= _min:
    mid = (_max + _min) // 2
    res = 0

    for i in budget:
        if mid < i:
            res += mid

        else:
            res += i

    if res > m:
        _max = mid - 1

    else:
        _min = mid + 1

print(_max)