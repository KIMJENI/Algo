import sys

n = int(sys.stdin.readline())
h = [int(sys.stdin.readline()) for i in range(n)]
stack, res = [],0

for i in range(n):
    while stack != [] and stack[-1] <= h[i]:
        stack.pop()
    stack.append(h[i])
    res+=len(stack)-1
print(res)
