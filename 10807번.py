#10807번
#정수 입력
n = int(input())
data = list(map(int,input().split()))
v = int(input())

count = 0

#데이터의 갯수만큼 for문 반복
for i in range(len(data)):
    #데이터와 정수v가 같으면 +1
    if data[i]==v:
        count+=1

print(count)
