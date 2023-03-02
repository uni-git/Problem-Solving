# N * M 크기의 직사각형 형태의 미로
# 미로에 여러 마리 괴물을 피해 탈출
# 동빈 (1,1) 미로의 출구 (N,M)의 위치
# 괴물이 있는 부분은 0, 괴물이 없는 부분은 1
# 탈출하기 위해 움직여야하는 최소 칸의 개수


# n, m 입력받기
# n, m= map(int, input().split())
#
#
# graph = []
# for i in range(n):
#     graph.append(list(map(int, input())))
#
# # dfs로 구현
# def dfs(x,y):
#     # 범위 (1,1) ~ (n,m) 제한 체크
#     if x < 1 or x > n or y < 1 or y > m:
#         return False
#
#     if graph[x][y] == 1:
#         graph[x][y] == 0
#         dfs(x-1,y)   # 상
#         dfs(x+1,y-1) # 하
#         dfs(x,y-1)   # 좌
#         dfs(x,y+1)   # 우
#         return True
#     return False
#
# result = 0
# for i in range(1, n+1):
#     for j in range(1,m+1):
#         if dfs(i,j) == True:
#             result += 1
# print(result)
#


# 최단 거리 문제는 bfs로 풀것
from collections import deque

def bfs(x,y):
    queue = deque()
    queue.append((x,y))
    # 큐가 빌때까지 반복하기
    while queue:
        x, y = queue.popleft()
        # 현재 위치에서 4가지 방향으로 위치 확인
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            # 미로 찾기 공간을 벗어난 경우 무시
            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue
            # 해당 노드를 처음 방문하는 경우에만 최단 거리 기록
            if graph[nx][ny] == 1:
                # print(graph[x][y])
                graph[nx][ny] = graph[x][y] + 1 # 직전 노드값의 거리값 1 증가(이동 칸수 카운트)
                # print(graph[nx][ny])

                queue.append((nx, ny))
    # 가장 오른쪽 아래까지의 최단 거리 반환
    return graph[n-1][m-1]

n, m = map(int, input().split())

graph = []
for _ in range(n):
    graph.append(list(map(int, input())))

dx = [-1,1,0,0]
dy = [0,0,-1,1]

print(bfs(0,0))
