#1158번

#N, K입력
N, K = map(int, input().split())

#배열 생성
arr = [i for i in range(1, N+1)]

#제거한 원소 저장
ans = []

#원을 도는 주기
num= K-1

#N번 만큼 for문 수행
for i in range(N):
    if len(arr)>num:
        ans.append(arr.pop(num))
        num+=K-1
        
    else: #len(arr)<=num
        '''
        한 바퀴를 다 돌았을 경우 리스트 길이를 주기로
        나눈 나머지를 인덱스로 하는 값을 제거
        '''
        num = num % len(arr)
        ans.append(arr.pop(num))
        num+=K-1

print('<', ', '.join(str(i) for i in ans), '>', sep = '')
