def stars(n):
    matrix = [] #별을 담을 리스트 선언
    for i in range(len(n) * 3):
        if i//len(n)==1:
            matrix.append(n[i % len(n)] + " " * len(n) + n[i % len(n)])

        else:
            matrix.append(n[i % len(n)] * 3)

    return matrix

resultStar = ['***', '* *', '***']

n = int(input())
count =0

while n!=3:
    n//=3
    count +=1

for _ in range(count):
    resultStar = stars(resultStar)

for j in resultStar:
    print(j)
