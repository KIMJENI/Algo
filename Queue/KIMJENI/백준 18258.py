import sys
from collections import deque

N = int(sys.stdin.readline())

##보통 큐는 선입선출 방식으로 작동
##양방향 큐가 있는 데 그것이 데크(deque)
q = deque()
count = 0

for i in range(N):
    cmd = sys.stdin.readline().split()

    if cmd[0] == 'push':
        #deque.append(item) : item을 데크의 오른쪽 끝에 삽입한다.
        q.append(cmd[1])
        count+=1

    elif cmd[0] == 'pop':
        if count == 0:
            print(-1)
        else:
            ##deque.popleft():데크의 왼쪽 끝 엘리먼트를 가져오는 동시에
            ##                데크에서 삭제한다.
            print(q.popleft())
            count-=1

    elif cmd[0] == 'size':
        print(count)

    elif cmd[0] == 'empty':
        if count == 0:
            print(1)
        else:
            print(0)

    elif cmd[0] == 'back':
        if count == 0:
            print(-1)
        else:
            print(q[len(q)-1])

    elif cmd[0] == 'front':
        if count == 0:
            print(-1)
        else:
            print(q[0])
