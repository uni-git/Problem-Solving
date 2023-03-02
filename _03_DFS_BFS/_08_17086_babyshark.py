# 문제
# 한칸에 아기상어 1마리 존재
# 칸의 안전거리는 가장 거리가 가까운 아기상어아의 거리
# 두칸의 거리 : 하나의 칸에서 다른 칸으로 가기 위해서 지나야하는 칸의 수
# ex) o | o | o | o 가 있으면 첫번째와 마지막칸 사이의 거리는 2
# 이동은 인접한 8방향이 가능
# 안전거리가 가장 큰 값을 구하기

# 왜 bfs 유형인가?
# 안전거리 : 상어로부터 가장 가까운 거리를 측정한 값이 안전거리이기 때문
# 그 거리가 가장 큰 것을 골라야 함


import sys
from collections import deque

n, m = map(int, sys.stdin.readline().split())

array = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]

dx = [-1, -1, -1, 0, 1, 0, 1, 1]
dy = [-1, 0, 1, 1, 1, -1, 0, -1]


queue = deque()

for i in range(n):
    for j in range(m):
        queue.append([i,j]) # 0,0 부터 탐색 시작

result = 0
while queue:
    x,y = queue.popleft()
    for d in range(8):
        nx = x + dx[d]
        ny = y + dy[d]
        if nx < 0 or ny < 0 or nx >= n or ny >= y: # 배열 범위 이탈
            continue
        if array[nx][ny] != 0: # 상어가 있는 노드
            continue
        # print(array)
        # print("nx : " + str(nx) + " ny :" + str(ny))
        queue.append([nx,ny])
        array[nx][ny] = array[x][y] + 1
        result = max(result, array[x][y] + 1)
print(result - 1) # 두개의 노드 사이의 거리를 구하는 것이기 때문

