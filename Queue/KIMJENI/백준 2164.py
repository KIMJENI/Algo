import sys
from collections import deque

N = int(input())
q = deque()

for i in range(1,N+1):
    q.append(i)

'''
deque.rotate(num) : 데크를 num만큼 회전한다.
                  ( 양수면 오른쪽, 음수면 왼쪽)
'''

while len(q)>1:  
    q.popleft()
    q.rotate(-1)

print(q.pop())
