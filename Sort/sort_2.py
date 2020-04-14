# 문제
# 0 또는 양의 정수가 주어졌을 때, 정수를 이어 붙여 만들 수 있는 가장 큰 수를 알아내 주세요.

# 예를 들어, 주어진 정수가 [6, 10, 2]라면 [6102, 6210, 1062, 1026, 2610, 2106]를 만들 수 있고,
# 이중 가장 큰 수는 6210입니다.

# 0 또는 양의 정수가 담긴 배열 numbers가 매개변수로 주어질 때,
# 순서를 재배치하여 만들 수 있는 가장 큰 수를 문자열로 바꾸어 return 하도록 solution 함수를 작성해주세요.

# 제한 사항
# numbers의 길이는 1 이상 100,000 이하입니다.
# numbers의 원소는 0 이상 1,000 이하입니다.
# 정답이 너무 클 수 있으니 문자열로 바꾸어 return 합니다.

# 입출력 예
# numbers	return
# [6, 10, 2]	6210
# [3, 30, 34, 5, 9]	9534330


def solution(numbers):
    answer = ''
    numbers = list(map(str, numbers)    # 문자열로 전환된 numbers
    num=[]

    for i in numbers:
        if len(i) == 1:
            num.append(i)
        elif len(i) == 2:
            k=int(i) // 10
            num.append(k)
        elif len(i) == 3:
            k=int(i) // 100
            num.append(i)
        else:
            k=int(i) // 1000
            num.append(i)

    for i in range(len(numbers)):
        n=max(num)
        if num.count(n) == 0:
            for k in numbers:
                if n in k:
                    answer += k
            num.remove(n)
        else:       # 3, 30, 34
            nlist = [x for x in numbers if n in x]  # 3,30,34
            for k in nlist:
                k 
    return answer

# 문자열에서 find?함수 search함수?

# num = [3, 34, 45, 27, 543, 33]
# nums = list(map(str, num))

# k = '3'
# for i in nums:
#     if k in i:
#         print(i)
