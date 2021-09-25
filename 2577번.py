#2577
#정수입력
A = int(input())
B = int(input())
C = int(input())

#문자로 형변환
mul = str(A*B*C)

#리스트로 변환
result = list(mul)

data = list('0123456789')

count = 0

#data*result의 개수 만큼 for문 반복
for i in range(len(data)):
    #count 초기화
    count = 0
    for j in range(len(result)):
        #data와 result이 같으면 +1
        if data[i] == result[j]:
            count+=1
    print(count)

