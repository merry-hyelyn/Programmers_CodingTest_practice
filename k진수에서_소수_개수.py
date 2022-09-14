import math


def convert_number(n, k):
    res = ''
    while n > 0:
        n, mod = divmod(n, k)
        res += str(mod)
    return res[::-1]


def is_prime(num):
    if num == 1:
        return False
    for i in range(2, int(math.sqrt(num)) + 1):
        if num % i == 0:
            return False
    return True


def solution(n, k):
    answer = 0
    num = convert_number(n, k)
    split_nums = num.split('0')
    for num in split_nums:
        if num and is_prime(int(num)):
            answer += 1
    return answer
