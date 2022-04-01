from sys import stdin

Stack_list = []
Stack_str = []
def push(X):
    global Stack_list
    Stack_list.append(X)
    Stack_str.append("+")

def pop():
    global Stack_list
    if not Stack_list:
        print("NO")
    else:
        Stack_list.pop()
        Stack_str.append("-")


N = int(stdin.readline())
Input_num = [0]*N
count = 0

for i in range(N):
    Input_num[i] = int(input())

for i in range(N):
    push(i + 1)

    while Input_num[count] == Stack_list[-1]:
        pop()
        count += 1
        if not Stack_list:
            break
if(count>=N):
    for i in range(len(Stack_str)):
        print(Stack_str[i])
else:
    print("NO")
