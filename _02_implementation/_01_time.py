# 완전 탐색(Brute Forcing)
# N 시가 주어졌을때, 3이 포함된 시각을 세아리기
# 하루는 84,000초이므로, 경우의 수 84,000가지
# 복잡도 고려할때 파이썬은 1초에 2천만번으로 계산할 수 있음

n = int(input())
cnt = 0
for i in range(n + 1):
    for j in range(60):
        for k in range(60):
            if '3' in str(i) + str(j) + str(k):
                cnt +=1
print(cnt)

