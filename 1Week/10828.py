from sys import stdin

Stack_list = []

def push(X):
    global Stack_list
    Stack_list.append(X)

def pop():
    global Stack_list
    if not Stack_list:
        print(-1)
    else:
        print(Stack_list.pop())

def size():
    global Stack_list
    print(len(Stack_list))

def empty():
    global Stack_list
    if not Stack_list:
        print(1)
    else: print(0)

def top():
    global Stack_list
    if not Stack_list:
        print(-1)
    else:
        print(Stack_list[-1])

N = int(stdin.readline())

for _ in range(N):
    Input_list = list(map(str, stdin.readline().split()))
    if(Input_list[0] == "push"):
        push(Input_list[1])
    elif(Input_list[0] == "pop"):
        pop()
    elif (Input_list[0] == "size"):
        size()
    elif (Input_list[0] == "empty"):
        empty()
    elif (Input_list[0] == "top"):
        top()

