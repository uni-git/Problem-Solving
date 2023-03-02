# 숫자로만 이루어진 문자열 S, 왼쪽부터 오늘쪽으로 하나씩 모든 숫자를 확인하며 숫자사이제 X 혹은 +을 넢어 결과적으로 만들어질 수 있는 가장 큰 수
# 0인경우 더하기
# 1인경우 더하기
data = input()

# 첫 번째 문자를 숫자로 변경해 대입
result = int(data[0])

for i in range(1,len(data)):
    # 두 수 중 하나라도 '0' 또는 '1'인 경우, 더하기 수행
    num = int(data[i])
    if num <= 1 or result <= 1: # 0,1이 첫번째 자리에 있는 경우, 가운데 있는 경우를 모두 생각해야함
        result += num
    else: result *= num
print(result)
