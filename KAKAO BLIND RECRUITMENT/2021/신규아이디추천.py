from collections import defaultdict


def solution(id_list, report, k):
    answer = []
    reporters = defaultdict(set)
    be_reported = defaultdict(set)
    count_reported = defaultdict(int)
    for user in report:
        u, s = user.split()
        reporters[u].add(s)
        if u not in be_reported[s]:
            be_reported[s].add(u)
            count_reported[s] += 1
    stopped_ids = []
    for user, count in count_reported.items():
        if count >= k:
            stopped_ids.append(user)
    for user in id_list:
        count = 0
        for stopped in stopped_ids:
            if stopped in reporters[user]:
                count += 1
        answer.append(count)
    return answer
