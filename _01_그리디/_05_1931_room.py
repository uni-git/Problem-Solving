# 한개의 회의실 N개의 회의에 대한 사용표 만들기

# 시작시간과 끝나는 시간을 비교하면됨
# 가장 많은 회의수를 알기 위해선 빨리 끝나는 회의 순서대로 정렬
# 시작시간을 기준으로 오름차순 : 최대한 많은 회의를 진행하려면 회의시간이 짧을 수록 유리하기 때문
# 종료시간을 기준으로 오름차순 : 가장 많은 회의수를 알기 위해선 빨리 끝나는 회의 순서대로 정렬


n= int(input())
time = []

for _ in range(n):
    start, end = map(int, input().split())
    time.append([start,end])

time = sorted(time, key=lambda a: a[0])
time = sorted(time, key=lambda a: a[1])

last = 0
cnt = 0

for i,j in time:
    if i>= last:
        cnt +=1
        last = j
print(cnt)
