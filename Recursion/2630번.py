
#첫 색상이 나머지 색상과 같은지 확인 후 틀린 것이 있으면,
#틀린 구역을 다시 네 구역으로 나누어 다시 색상이 같은 것을 확인

import sys

#변수길이 입력
N = int(sys.stdin.readline())
#배열
paper = [list(map(int, sys.stdin.readline().split())) for _ in range(N)] 

result = []

def solution(x, y, N) :
  color = paper[x][y]
  for i in range(x, x+N) :
    for j in range(y, y+N) :
      if color != paper[i][j] :
        solution(x, y, N//2)
        solution(x, y+N//2, N//2)
        solution(x+N//2, y, N//2)
        solution(x+N//2, y+N//2, N//2)
        return
  if color == 0 :
    result.append(0)
  else :
    result.append(1)


solution(0,0,N)
print(result.count(0))
print(result.count(1))
