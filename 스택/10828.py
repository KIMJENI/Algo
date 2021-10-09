import sys

#정수 n입력
n = int(sys.stdin.readline())

stack=[]


for i in range(n):
    command = sys.stdin.readline().split()

    #정수 x를 스택에 넣음
    if command[0]=='push':
        stack.append(command[1])
    
    #스택에서 최상단에 있는 정수를 빼고, 그 수를 출력
    #스택이 비어있으면 -1을 출력
    elif command[0]=='pop':
        if len(stack)==0:
            print(-1)
        else:
            print(stack.pop())

    #스택에 들어있는 정수의 개수 출력
    elif command[0] == 'size':
        print(len(stack))

    #스택이 비어있으면1, 아니면 0을 출력
    elif command[0] == 'empty':
        if len(stack)==0:
            print(1)
        else:
            print(0)

    #스택에서 최상단에 있는 정수를 출력
    #스택이 비어있으면 -1을 출력
    elif command[0] == 'top':
        if len(stack)==0:
            print(-1)
        else:
            print(stack[-1])

