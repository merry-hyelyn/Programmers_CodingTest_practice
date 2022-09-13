from collections import Counter


def get_point_value(dot):
    point = Counter(dot)
    return [k for k, v in point.items() if v == 1]


def solution(v):
    answer = []
    dots = list(zip(*v))
    x = get_point_value(dots[0])
    y = get_point_value(dots[1])
    return x + y

# def solution(v):
#     x = v[0][0]^v[1][0]^v[2][0]
#     y = v[0][1]^v[1][1]^v[2][1]
#     return [x, y]
