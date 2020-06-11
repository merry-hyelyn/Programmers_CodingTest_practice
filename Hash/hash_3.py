def solution(clothes):
    answer = 1
    cloth_hash = {}
    for name, kind in clothes:
        if kind in cloth_hash:
            cloth_hash[kind] += 1
        else:
            cloth_hash[kind] = 1

    for v in cloth_hash.values():
        answer *= (v+1)
    return answer - 1
