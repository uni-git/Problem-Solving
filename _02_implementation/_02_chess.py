# 체스에서 나이트의 이동 범위
# 8 * 8
# 수평으로 두칸 이동한 뒤 수직으로 한칸
# 수직으로 두칸 이동한 뒤 수평으로 한칸
x, y = map(int,input().split())
# 이동 방향의 경우의 수 : 8가지
dx = [-2,-2,-1,1,2,2,1,-1]
dy = [-1,1,2,2,1,-1,-2,-2]

# 범위 벗어나면 방향 이동 X
# 완전 탐색
cnt = 0
for i in range(8):
    nx = x + dx[i]
    ny = y + dy[i]
    if nx < 0 or ny < 0 or nx > 7 or ny > 7:
        continue
    cnt += 1
print(cnt)


# 다른 방법
# 체스판의 좌표평면 표시 방법 행은 a~h , 열은 1~8
# 입력값 예시 a1
# 현재 나이트 위치받기
input_data = input()
row = int(input_data[1])
column = int(ord(input_data[0])) - int(ord('a')) + 1 # ord : 입력받은 문자의 아스키 코드 값을 반환

# 나이트가 이동할 수 있는 8가지 방향(dx,dy 별도로 생성하지 않고 하나로 만든 방법)
steps = [(-2,-1),(-1,-2),(1,-2),(2,-1),(2,1),(1,2),(-1,2),(-2,1)]

# 8가지 방향에 대하여 각 위치로 이동이 가능한지 확인
result = 0
for s in steps:
    # 이동하고자 하는 위치 확인
    next_row = row + steps[0]
    next_column = column + steps[1]
    # 해당 위치로 이동이 가능하다면 카운트 증가
    if next_row >= 1 and next_row <= 8 and next_column >=1 and next_column <=8 :
        result += 1
print(result)