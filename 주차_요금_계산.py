import math
from collections import defaultdict


def calculate_total_fee(time, fees):
    basic_time, basic_fare, unit, unit_fare = fees
    if time < basic_time:
        return basic_fare
    return basic_fare + math.ceil((time - basic_time) / unit) * unit_fare


def calculate_total_time(values):
    return sum([values[i+1] - values[i] for i in range(0, len(values), 2)])


def get_timestamp(time):
    hour, minute = list(map(int, time.split(':')))
    return hour * 60 + minute


def solution(fees, records):
    answer = []
    record_by_car = defaultdict(list)
    last_time = 1439  # 23:59
    for record in records:
        time, car, _ = record.split()
        timestamp = get_timestamp(time)
        record_by_car[car].append(timestamp)
    record_by_car = sorted(record_by_car.items(), key=lambda x: x[0])
    for _, values in record_by_car:
        if len(values) % 2 != 0:
            values.append(last_time)
        total_time = calculate_total_time(values)
        answer.append(calculate_total_fee(total_time, fees))
    return answer
