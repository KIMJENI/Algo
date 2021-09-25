#10808번
#문자열 s 입력
s = list(map(str, input()))

#alphabet리스트
alphabet = list('abcdefghijklmnopqrstuvwxyz')

#배열 array를 알파벳 갯수 만큼 0으로 초기화
array = [0 for i in range(len(alphabet))]

#alphabet리스트의 인덱스와 문자열 s의 인덱스가 같으면 +1 
for i in range(len(s)):
    if array[alphabet.index(s[i])] >= 0:
        array[alphabet.index(s[i])]+=1

for j in array:
    print(j, end = " ")
    
    

#----------------------------------------------------------------
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



#--------------------------------------------------------------------
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


#-----------------------------------------------------------------------
#11328번
n = int(input())
 
for i in range(n):
    a, b = input().split()
    a = ''.join(sorted(a))
    b = ''.join(sorted(b))
 

    for i in range(len(a)):
        if a[i] != b[i]:
            flag = False
            break
        else:
            flag = True

    if flag:
        print('Possible')
    else:
        print('Impossible')
        


#-----------------------------------------------------------------------
#13300번
n, k = list(map(int,input().split()))

w = [0]*1000
m = [0]*1000

for i in range(n):
    s, y = list(map(int,input().split()))
    if s==0:
        w[y] += 1
    else:
        m[y] +=1

for i in range(1, 7):
    if(w[i]%k==0):
        w[i] = w[i]//k
    else:
        w[i] = w[i]//k+1

    if(m[i]%k==0):
        m[i] = m[i]//k
    else:
        m[i] = m[i]//k+1

result = sum(w) + sum(m)
print(result)
            



#-----------------------------------------------------------------------
#1475번
n =input()

num = list('0123456789')
array = [0 for i in range(10)]

for i in range(len(n)):
    if n[i] == '9':
        array[6]+=1
    array[num.index(n[i])]+=1

if array[6]  % 2 == 0:
        array[6] = array[6] // 2
        array[9] = array[6] // 2

else:
    array[6] = (array[6] // 2) + 1
    array[9] = (array[6] // 2) + 1


result = 0

for j in array:
    if j > result:
        result = j
print(result)



#---------------------------------------------------------------------------
#!!!!!!
#1919번
a = list(input())
b = list(input())

result = 0

intersection = set(a)&set(b)
symmertirc_difference= set(a)^set(b)
for c in symmetric_difference:
    set += a.count(c)+b.count(c)

for c in intersection:
    result += abs(a.count(c)-b.count(c))

print(result)



#--------------------------------------------------------------------------
#3273번
n = int(input())
num = list(map(int, input().split()))
num.sort()#오름차순정렬
x = int(input())

count = 0

left, right = 0, n-1

while left != right:
    if num[left]+num[right]==x:
        count += 1
        left+=1

    elif num[left]+num[right]>x:
        right-=1
    else:
        left+=1
print(count)










