
n, k = map(int,input().split())

# data = list()
# for _ in range(n):
#     data.append(int(input()))

# 리스트 컴프리핸션
data = [int(input()) for _ in range(n)]
# print(data)
cnt = 0
data.reverse()
for i in data:
    if k // i >= 1:
        cnt += k // i
        k = k % i
        continue
    else : pass
print(cnt)
