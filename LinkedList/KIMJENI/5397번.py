#5397번

import sys
#테스트 케이스 수 입력
n=int(input())

for _ in range(n):
    #문자열 입력
    case = list(sys.stdin.readline().strip())
    
    string1 = []
    string2 = []

    #문자열 길이 만큼 for문 반복
    for i in case:

        if i=='-':
            if string1:
                string1.pop()

        elif i=='<':
            if string1:
                string2.append(string1.pop())

        elif i=='>':
            if string2:
                string1.append(string2.pop())
                
        else:
            string1.append(i)


    #string2는 stack에 입력순서의 역순으로 쌓여 있으므로, 재배열
    print(''.join(string1+string2[::-1]))

