# def solution(array, commands):
#     answer = []
#     for h in range(len(commands)):
#         i = commands[h][0]
#         j = commands[h][1]
#         k = commands[h][2]
#         a = array[i - 1: j]
#         a.sort()
#         answer.append(a[k - 1])
#     return answer


# array = [1, 5, 2, 6, 3, 7, 4]
# commands = [[2, 5, 3], [4, 4, 1], [1, 7, 3]]
# print(solution(array, commands))
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
