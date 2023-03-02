# 문자열 재정렬
# 알파벳 대문자와 숫자(0~9)로만 구성된 문자열이 입력으로 주어짐
# 이때 모든 알파벳을 오름차순으로 정렬하여 이어서 출력, 그 뒤 모든 숫자를 더한 값을 이어서 출력
# 예) K1KA5CB7 -> ABCKK13 출력


# print(ord('A'))
#
# a = list(map(str,input()))
# a.sort()
# print(a)
# result_alphabet = list()
# result_number = list()
# for i in a:
#     # 65보다 큰것들을 먼저 정렬하고 작은것들은 마지막에 정렬
#     if ord(i) >= 65:
#         result_alphabet.append(i)
#     else:
#         result_number.append(i)
#
# print(result_alphabet + result_number)
#
# # 리스트에서 str로 변경하기
# result_str = ""
# for i in result_alphabet:
#     result_str += i
# for i in result_number:
#     result_str += i
#
# print(result_str)

# 문자열이 입력되었을때 하나씩 확인
# 숫자인 경우 따로 합계 계산
# 문자인 경우 리스트에 저장
# 알파벳은 정렬해 출력, 합계를 뒤에 붙임

data = input()
result = []
value = 0

# 문자를 하나씩 확인
for x in data:
    # 알파벳인 경우 결과 리스트에 삽입
    if x.isalpha():
        result.append(x)
    # 숫자는 따로 더하기
    else:
        value += int(x)
# 알파벳을 오름차순으로 정렬
result.sort()

# 숫자가 하나라도 존재하는 경우 가장 뒤에 삽입
if value != 0:
    result.append(str(value))

# 최종 결과 출력(리스트를 문자열로 변환하여 출력)
print(''.join(result))
