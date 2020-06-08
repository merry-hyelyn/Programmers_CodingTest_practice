phone_book = [119, 97674223, 1195524421]
def solution(phone_book):
    phone_book = list(map(str, phone_book))
    min = 20
    for num in phone_book:
        if min > len(num):
            min = len(num)
            min_num = num

    phone_book.remove(min_num)
    for k in phone_book:
        if min_num in k[:min]:
            return False

    return True