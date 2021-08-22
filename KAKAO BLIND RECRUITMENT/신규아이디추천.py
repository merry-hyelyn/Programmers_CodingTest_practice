def step_two(new_id):
    condition = ['-', '_', '.']
    temp = new_id
    for i in temp:
        if not i.isdigit() and i not in condition and not i.isalpha():
            new_id = new_id.replace(i, '')
    return new_id


def step_three(new_id):
    prev = ''
    target = ''
    temp = new_id
    for w in temp:
        if w == '.':
            if prev:
                print(prev)
                if prev == w:
                    target += prev
                else:
                    if target:
                        target += prev
                        print("target : ", target)
                        new_id = new_id.replace(target, '.')
                        target = ''
        prev = w
    return new_id


def solution(new_id):
    answer = ''
    print('0 : ', new_id)

    new_id = new_id.lower()
    print("1 : ", new_id)

    new_id = step_two(new_id)
    print("2 : ", new_id)

    new_id = step_three(new_id)
    print("3 : ", new_id)
    return answer


solution("...!@BaT#*..y.abcdefghijklm")
