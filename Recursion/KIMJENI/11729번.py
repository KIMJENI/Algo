#num개의 원반을 옮기기 위해서는 num-1개의 원반을 이웃한 b으로 옮겨야 한다.
#가장 큰 원반이 c로 간다.
#이제 b에서 n-1개의 원반을 c로 옮긴다.


def hanoi(num,a,b,c):
    if(num == 1):
        #a번째 탑의 가장 위에 있는 원판을 c번째 탑의 가장 위로 옯긴다.
        print(a, c)
    else:
        # a = start, b= to, c = end
        #n-1개의 원판을 1번에서 2번으로 옮김
        hanoi(num-1,a,c,b)
        #남은 1개의 원판을 1번에서 3번으로 옮김(기준점을 바꿔줌)
        print(a,c)
        #n-1개의 원판을 2번에서 3번으로 옮김.
        hanoi(num-1,b,a,c)

num = int(input())
#옮긴횟수
print((2**num)-1)
hanoi(num,1,2,3)
