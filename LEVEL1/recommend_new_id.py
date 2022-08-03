import re


def add_id_length(new_id):
    pattern = new_id[-1]
    while len(new_id) < 3:
        new_id += pattern
    return new_id


def cut_id_length(new_id):
    if len(new_id) >= 16:
        new_id = new_id[:15].rstrip('.')
    return new_id


def replace_empty_string(new_id):
    return new_id if new_id else "a"


def remove_both_side_dot(new_id):
    return new_id.strip('.')


def replace_continuous_dot(new_id):
    pattern = ".."
    while new_id.count(pattern):
        new_id = new_id.replace(pattern, ".")
    return new_id


def remove_special_char(new_id):
    pattern = "[^0-9a-z-_.]"
    return re.sub(pattern, "", new_id)


def upper_to_lower(new_id):
    return new_id.lower()


def solution(new_id):
    first = upper_to_lower(new_id)
    second = remove_special_char(first)
    third = replace_continuous_dot(second)
    fourth = remove_both_side_dot(third)
    fifth = replace_empty_string(fourth)
    sixth = cut_id_length(fifth)
    answer = add_id_length(sixth)
    return answer
