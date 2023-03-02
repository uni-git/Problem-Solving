# 1로 만들기
# N이 1이 될 때가지 과정 중 하나를 반복 수행함.
# 1. N에서 1을 뺌
# 2. N을 K로 나눔

# 반복문
# 2번의 경우가 아닌 경우
# 1번 진행
# import time
# # n = int(input())
# # k = int(input())
# n, k = map(int, input().split())
# start = time.time()
# cnt = 0
# while n != 1:
#     if n % k != 0:
#         n -= 1; cnt += 1
#
#     else : n = n // k; cnt += 1;
# print(start - time.time())
# print(cnt)
# 정당성 : 가능한 최대한 많이 나누는 작업이 최적의 해를 항상 보장함
# k가 2보다 이상 크면 N이 아무리 큰 수여도, 1을 빼는 것보다 K로 나누는것이 기하급수적으로 빠르게 줄일 수 있기 때문

# 시간복잡도 (N)

# 시간복잡도 (log) 줄이기
# 26 3
n, k = map(int, input().split())

result = 0
while True:
    target = (n//k) * k # n과 최대 가까운 수  24
    result += (n - target) # 2
    n = target # n = 24

    if n < k: # n이 k보다 작을 때 반복문 탈출
        break
    result += 1 # 3
    n //= k # n = 8

result += n-1
print(result)
