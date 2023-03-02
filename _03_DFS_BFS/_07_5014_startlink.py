# F : 최고층
# G : 스타트링크
# S : 강호 위치
# U : +U만큼 이동
# D : -U만큼 이동
# 갈수 없는 경우 use the stairs
#
import sys
from collections import deque
f, s, g, u, d = map(int, sys.stdin.readline().split())

queue = deque()
def bfs():

    queue.append(s)
    visited[s] = 1
    while queue:
        loc = queue.popleft()

        # 탈출 조건
        if loc == g:
            print(visited[loc] - 1) # 첫번째 위치 1 빼고 계산
            return str
        for d_loc in (loc + u, loc - d):
            if 1 <= d_loc <= f and visited[d_loc] == 0:
                queue.append(d_loc)
                visited[d_loc] = visited[loc] + 1

    if visited[g] == 0 : return "use the stairs"

visited = [0] * (f+1) # 1층 부터 시작
bfs()
#
from collections import deque


f, s, g, u, d = map(int, input().split())


def bfs(start, goal):
    q = deque()
    visited = [-1] * (f + 1)

    q.append(start)
    visited[start] = 0

    while q:
        x = q.popleft()

        if x == goal:
            return visited[x]

        for nx in (x + u, x - d):
            if 0 < nx <= f and visited[nx] == -1:
                q.append(nx)
                visited[nx] = visited[x] + 1

    return "use the stairs"


print(bfs(s, g))
