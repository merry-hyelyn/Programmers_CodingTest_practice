# def solution(phone_book):
#     hash_table = {}
#     for n in phone_book:
#         for k in hash_table.keys():
#             if n in k:
#                 hash_table[k] += 1
#             else:
#                 hash_table[n] += 1
#     print(hash_table)
#     return answer


# print(solution(["119", "23454", "1193423"]))

hash_table = {}
phone_book = ["119", "32434", "1193425"]
for n in phone_book:
    hash_table[n] += 1
for k, v in hash_table.items():
    print(k, v)
