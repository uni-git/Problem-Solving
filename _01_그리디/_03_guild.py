from collections import Counter

data = list(map(int,input().split(" ")))

counter = Counter(data)
# print(dict(counter))
d = dict(counter)

result = 0
for i in d: # key
    # print(d[i]) # count 갯수
    result += d[i] // i
print(result)



# 다른 방법
data.sort()
result = 0
count = 0
for i in data: #공포도가 낮은 것부터 하나씩확인
    count += 1 # 현재 그룹 해당 모험가를 포함시키기
    if count >= i:# 현재 그룹에 포함된 모험가 수가 현재공포도 이상이라면, 그룹 결성
        result += 1 # 총 그훕의 수 증가
        count =0 # 현재 그룹에 포함된 모험가의 수 초기화

print(result)
