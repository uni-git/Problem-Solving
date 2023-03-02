# n * M 얼음 틀
# 구멍이 뚫려 있는 부분은 0, 칸막이가 있는 부분은 1
# 구멍이 뚫려 있는 부분끼리 상,하, 좌, 우로 붙어있는 경우 서로 연결되어 있는 것
# 총 아이스크림의 개수 구하기
# BFS : 0노드 주변의 노드가 1인 경우 아이스크림 1개로 간주
# 모든 노드의 방문처리를 진행하면서 방문처리 되는 경우만 카운트 하면됨

# dfs로 특정 노드를 방문하고 연결된 모든 노드들도 방문
def dfs(x,y):
    # 주어진 범위를 벗어나는 경우에는 즉시 종료
    if x <= -1 or x >=n or y <= -1 or y >= m:
        return False
    if graph[x][y] == 0:
        # 해당 노드 방문 처리
        graph[x][y] = 1
        # 상, 하, 좌, 우의 위치들도 모두 재귀적으로 호출
        dfs(x - 1, y)
        dfs(x, y - 1)
        dfs(x + 1, y)
        dfs(x, y + 1)
        return True
    return False

# N, M을 공백을 기준으로 구분하여 입력받기
n, m= map(int, input().split())

# 2차원 리스트의 맵 정보 입력 받기
graph = []
for i in range(n):
    graph.append(list(map(int, input())))

# 모든 노드(위치)에 대하여 음료수 채우기
result = 0
for i in range(n):
    for j in range(m):
        # 현재 위치에서 DFS 수행
        if dfs(i,j) == True:
            result += 1
print(result)



