def solution(array, commands):
    answer = []
    for command in commands:
        i, j, k = command
        new_array = array[i - 1: j]
        new_array.sort()
        answer.append(new_array[k - 1])
    return answer


a = [1, 5, 2, 6, 3, 7, 4]
c = [[2, 5, 3], [4, 4, 1], [1, 7, 3]]
print(solution(a, c))
