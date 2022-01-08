n = int(input())
stack = []
op = []
flag = 0
count = 1

for i in range(n):
    num = int(input())

    #입력한 수를 만날 때 까지 오름차순으로 push
    while count<=num:
        stack.append(count)
        op.append('+')
        count+=1
    #입력한 수를 만나면 while문을 벗어남
        
    if stack[-1] == num:
        stack.pop()
        op.append('-')
    
    else:
        print('No')
        flag = 1
        break


if flag == 0:
    for i in op:
        print(i)

