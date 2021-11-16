from collections import deque
import sys
input = sys.stdin.readline

def push_front(x):
    dq.appendleft(x)

def push_back(x):
    dq.append(x)

def pop_front():
    return dq and dq.popleft() or -1

def pop_back():
    return dq and dq.pop() or -1

def size():
    return len(dq)

def empty():
    return not dq and 1 or 0

def front():
    return dq and dq[0] or -1

def back():
    return dq and dq[-1] or -1


N = int(input())
dq = deque([])


for i in range(N):
    cmd = input().split()
    if 'push_front' in cmd:
        push_front(cmd[1])

    elif 'push_back' in cmd:
        push_back(cmd[1])

    elif 'pop_front' in cmd:
        print(pop_front())

    elif 'pop_back' in cmd:
        print(pop_back())

    elif 'size' in cmd:
        print(size())

    elif 'empty' in cmd:
        print(empty())

    elif 'front' in cmd:
        print(front())

    else:
        print(back())
