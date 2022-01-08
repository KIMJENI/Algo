
if __name__ == '__main__':
    n = int(input())
    top_list = list(map(int, input().split()))
    #최대값을 저장한 리스트
    stack = []
    #수신 탑 인덱스 저장
    result = []

    for i in range(n):
        while stack:
            #수신 가능한 상황
            if stack[-1][1]>top_list[i]:
                result.append(stack[-1][0]+1)
                break
            else:
                stack.pop()

        if not stack:
            result.append(0)
        stack.append([i, top_list[i]])

    print(' '.join(map(str, result)))
