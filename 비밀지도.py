def solution(n, arr1, arr2):
    answer = []
    for a, b in list(zip(arr1, arr2)):
        answer.append(bin(a | b)[2:].zfill(
            n).replace('0', ' ').replace('1', '#'))
    return answer


print(solution(6, [46, 33, 33, 22, 31, 50], [27, 56, 19, 14, 14, 10]))
