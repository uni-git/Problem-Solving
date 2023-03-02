# n * n 정사각형 공간 위에 있음
# 가장 왼쪽 위 좌표는 (1,1)

# 입력받기
n = int(input())
x, y = 1, 1
plans = input().split()

# (L,R,U,D) 기준
dx = [0,0,-1,1]
dy = [-1,1,0,0]

move_types = ['L','R','U','D']
# 이동 계획 하나씩 확인하기
for p in plans:
    # 이동 후 좌표 구하기
    for i in range(len(move_types)):
        if p == move_types[i]:
            nx = x + dx[i]
            ny = y + dy[i]
    # 공간을 벗어나는 경우 무시
    if nx < 1 or ny < 1 or nx > n or ny > n:
        continue
    # 이동
    x,y = nx, ny
print(x, y)