#입력 받을 스택 리스트 안의 총 숫자의 수
k = int(input())

#스택 리스트
stack = []

for i in range(k):
    num = int(input())
    #num이 0이면
    if(num == 0):
        stack.pop()
        
    #그렇지 않다면 스택에 저장
    else:
        stack.append(num)

print(sum(stack))
