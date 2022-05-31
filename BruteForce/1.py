# 수포자는 수학을 포기한 사람의 준말입니다. 수포자 삼인방은 모의고사에 수학 문제를 전부 찍으려 합니다. 수포자는 1번 문제부터 마지막 문제까지 다음과 같이 찍습니다.

# 1번 수포자가 찍는 방식: 1, 2, 3, 4, 5, 1, 2, 3, 4, 5, ...
# 2번 수포자가 찍는 방식: 2, 1, 2, 3, 2, 4, 2, 5, 2, 1, 2, 3, 2, 4, 2, 5, ...
# 3번 수포자가 찍는 방식: 3, 3, 1, 1, 2, 2, 4, 4, 5, 5, 3, 3, 1, 1, 2, 2, 4, 4, 5, 5, ...

# 1번 문제부터 마지막 문제까지의 정답이 순서대로 들은 배열 answers가 주어졌을 때, 가장 많은 문제를 맞힌 사람이 누구인지 배열에 담아 return 하도록 solution 함수를 작성해주세요.

# 제한 조건
# 시험은 최대 10,000 문제로 구성되어있습니다.
# 문제의 정답은 1, 2, 3, 4, 5중 하나입니다.
# 가장 높은 점수를 받은 사람이 여럿일 경우, return하는 값을 오름차순 정렬해주세요.
# 입출력 예
# answers	return
# [1,2,3,4,5]	[1]
# [1,3,2,4,2]	[1,2,3]


from collections import defaultdict
from re import M


def solution(answers):
    answer_count = defaultdict(int)
    giveup_math_people_answer = {
        1: [1, 2, 3, 4, 5],
        2: [2, 1, 2, 3, 2, 4, 2, 5],
        3: [3, 3, 1, 1, 2, 2, 4, 4, 5, 5],
    }
    for idx, answer in enumerate(answers):
        for i in range(len(giveup_math_people_answer.keys())):
            if giveup_math_people_answer[i+1][idx] == answer:
                answer_count[i+1] += 1
    ordered_dict = dict(sorted(answer_count.items(),
                        key=lambda x: (-x[1], x[0])))
    max_value = 0
    result = []
    for key, value in ordered_dict.items():
        if max_value <= value:
            result.append(key)
            max_value = value
        else:
            break
    return result


def main():
    tests = (
        {
            'parameters': [1, 2, 3, 4, 5],
            'result': [1]
        },
        {
            'parameters': [1, 3, 2, 4, 2],
            'result': [1, 2, 3]
        }
    )
    for test in tests:
        if test['result'] == solution(test['parameters']):
            print(f"{test['parameters']}는 성공!")


if __name__ == "__main__":
    main()
