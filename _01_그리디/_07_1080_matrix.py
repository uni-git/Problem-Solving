# 그리디 알고리즘인 이유
# 3 * 3 행렬을 순차적으로 비교하는 방법이 최선책이기 때문
# 1. 3 * 3 행렬을 기준으로 비교하는 범위는 (n-3,m-3)
# 2. A의 첫번째 3*3 행렬의 값과 B의 첫번째 3*3행렬의 값이 동일하지 않으면 A 행렬을 뒤집는다
# 3. 다음 행렬도 동일하게 뒤집는다
# 4. 뒤집은 A 행렬과 B 행렬의 값을 비교한다

def reverse(x,y):
    for i in range(x,x+3):
        for j in range(y,y+3):
            a[i][j] = 1 - a[i][j]

def check():
    for i in range(n):
        for j in range(m):
            if a[i][j] != b[i][j]:
                return False
                break
    return True

n, m = map(int,input().split()) # 행,열

a = [list(map(int,list(input()))) for _ in range(n)]
b = [list(map(int,list(input()))) for _ in range(n)]

count = 0

# 행렬 비교
for i in range(n-2): # 행
    for j in range(m-2): # 열
        if a[i][j] != b[i][j]:
            reverse(i,j)
            count += 1
if check():
    print(count)
else:print("-1")
