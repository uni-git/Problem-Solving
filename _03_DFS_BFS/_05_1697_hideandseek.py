from collections import deque
#
#
#
# # 곱하기, 빼기, 더하기 동시 실행
# # 초 더하기
# # targer number와 동일 한지 확인
# # 동일한 값이 없으면 반복
#
# n, k = map(int,input().split())
# max = 100000
# visited = [0] * (max + 1)
#
# def bfs():
#     queue = deque()
#     queue.append(n)
#
#     while queue:
#         tmp =[]
#         x = queue.popleft()
#
#         if x == k:
#             print(visited[x])
#             break
#         if x != k:
#             tmp.append(x + 1)
#             tmp.append(x - 1)
#             tmp.append(x * 2)
#
#         queue = tmp
#             # print(queue)
#     return False
#
# bfs()

import sys
from collections import deque

def bfs(x):
    q = deque([x])
    while q:
        x = q.popleft()
        if x == k:
            return array[x]
        for nx in (x-1, x+1, 2*x):
            if 0 <= nx < MAX and not array[nx]: # and not array[nx] 다음 방문할 노드의 방문 여부
                array[nx] = array[x] + 1 # array[nx] : 이동거리(초) 저장
                q.append(nx)


MAX = 100001
n, k = map(int, sys.stdin.readline().split())
array = [0] * MAX
print(bfs(n))

