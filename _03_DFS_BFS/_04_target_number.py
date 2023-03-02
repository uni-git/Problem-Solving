def solution(numbers, target):

    answer = 0
    leaves = [0]
    for n in numbers:
        tmp = []
        for parent in leaves:
            tmp.append(parent+n)
            tmp.append(parent-n)
        leaves = tmp
    for leaf in leaves:
        if leaf == target:
            answer += 1

    return answer

print(solution([4,1,2,1], 4))