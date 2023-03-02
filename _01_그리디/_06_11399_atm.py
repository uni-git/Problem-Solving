n = int(input())

a = list(map(int, input().split()))

a.sort()

result= 0
result_list = list()
for i in a:
    result = result + i
    result_list.append(result)
print(sum(result_list))
