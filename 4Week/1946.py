import sys

T = int(sys.stdin.readline())

for i in range(0, T):
    count = 1
    people = []

    N = int(input())
    for i in range(N):
        Paper, Interview = map(int, sys.stdin.readline().split())
        people.append([Paper, Interview])

    people.sort()
    max = people[0][1]

    for i in range(1, N):
        if max > people[i][1]:
            count += 1
            max = people[i][1]

    print(count)