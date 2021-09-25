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
