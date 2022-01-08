#1406
import sys
#문자열 입력
string1 =list(input())
string2=[]

#명령어 개수 입력
m=int(input())

#명령어 개수 만큼 for문 수행
for i in range(m):
    #명령어 입력
    command = sys.stdin.readline().strip().split()

    try:
        if command[0]=='L':
            string2.append(string1.pop())

        elif command[0]=='D':
            string1.append(string2.pop())

        elif command[0]=='B':
            string1.pop()
            
        elif command[0]=='P':
            string1.append(command[1])

    except:
        pass


#string2는 stack에 입력순서의 역순으로 쌓여 있으므로, 재배열
print(''.join(string1+string2[::-1]))
