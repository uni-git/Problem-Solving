# 배열 돌리기
# 회전 번호에 따라 좌표 변경해주기
def calc_1():
    # 행만 변경됨
    temp = [[0] * m for _ in range(n)]
    for i in range(n):
        temp[i] = arr[n-1-i]
    return temp

def calc_2():
    temp = [[0] * m for _ in range(n)]
    for i in range(n):
        for j in range(m):
            temp[i][j] = arr[i][m-1-j]
    return temp

def calc_3(arr, n, m):
    temp =[[0] * m for _ in range(n)]
    for i in range(n):
        for j in range(m):
            temp[i][j] = arr[n-1-j][i]
    return temp

def calc_4(arr, n, m):
    temp = [[0] * m for _ in range(n)]

    for i in range(n):
        for j in range(m):
            temp[i][j] = temp[j][m-1-i]
        return temp


def calc_5(arr, n, m):
    temp =[[0] * m for _ in range(n)]
    for i in range(n//2) :
        for j in range(m//2):
            temp[i][j + m //2] = arr[i][j]
    for i in range(n//2):
        for j in range(m //2, m):
            temp[i+n // 2][j] = arr[i][j]
    for i in range(n//2,n):
        for j in range(m//2,m):
            temp[i][j -m//2] = arr[i][j]
    for i in range(n//2,n):
        for j in range(m//2):
            temp[i-n//2][j] = arr[i][j]

def calc_6():
    temp = [[0]* m for _ in range(n)]
    for i in range(n //2):
        for j in range(m//2):
            temp[i+n // 2][j] = arr[i][j]
    for i in range(n//2,n):
        for j in range(m//2):
            temp[i][j+m//2] = arr[i][j]
    for i in range(n//2,n):
        for j in range(m//2):
            temp[i][j+m//2] = arr[i][j]
    for i in range(n//2):
        for j in range(m//2,m):
            temp[i][j-m//2] = arr[i][j]
    return temp

n, m, r = map(int,input().split())

arr = [list(map(int, input().split())) for _ in range(n)]
operation = list(map(int, input().split()))

for oper in operation:
    # 1. 배열 상하 반전
    if oper == 1: arr = calc_1()
    # 2. 배열 좌우 반전
    elif oper == 2: arr = calc_2()
    # 3. 오른쪽 90도 회전
    elif oper == 3:
        arr = calc_3(arr, n, m);
        n,m = m,n  # 디버깅 해보기
    # 4. 왼쪽 90도 회전
    elif oper == 4:
        arr = calc_4(arr, n, m);
        n,m = m,n  # 디버깅 해보기
    # 5. 4분면 시계방향으로 이동
    elif oper == 5:
        arr = calc_5()
    # 6. 4분면 반시계방향으로 이동
    elif oper == 6:
        arr = calc_6()








