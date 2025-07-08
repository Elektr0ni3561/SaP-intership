"""
Необходимо разработать метод connect_dicts(dict1, dict2), который соединит два
переданных словаря, значениями ключей в которых являются числа, и вернет
новый словарь, полученный по следующим правилам:
    • приоритетными являются ключи того словаря, сумма значений ключей
    которого больше (если суммы значений ключей будут равны, то второй
    словарь считается более приоритетным)
    • ключи со значениями меньше 10 не должны попасть в финальный
    словарь
    • получившийся словарь должен вернуться упорядоченным по значениям
    ключей в порядке возрастания.
"""

def connect_dicts(dict1, dict2):
    priority, secondary = (dict2, dict1) if sum(dict2.values()) >= sum(dict1.values()) else (dict1, dict2)
    result = {}
    for key, value in priority.items():
        if value >= 10:
            result[key] = value
    for key, value in secondary.items():
        if key in result:
            continue
        if value >= 10:
            result[key] = value

    return dict(sorted(result.items(), key=lambda x: (x[1], x[0])))


if __name__ == "__main__":
    print(connect_dicts({"a": 2, "b": 12}, {"c": 11, "e": 5}))              # => { "c": 11, "b": 12 }
    print(connect_dicts({"a": 13, "b": 9, "d": 11}, {"c": 12, "a": 15}))    # => { d: 11, "c": 12, "a": 13 }
    print(connect_dicts({"a": 14, "b": 12}, {"c": 11, "a": 15}))            # => { "c": 11, "b": 12, "a": 15 }
