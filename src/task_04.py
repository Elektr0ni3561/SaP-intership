"""
Дан список целых чисел. Необходимо разработать метод sort_list(list), который
поменяет местами все минимальные и максимальные элементы массива, а также
добавит в конец массива одно минимальное значение из него.
"""

def sort_list(_list=None):
    if _list is None or len(_list) == 0:
        return []

    minimum = None
    maximum = None

    for i in _list:
        if minimum is None or i < minimum:
            minimum = i
        if maximum is None or i > maximum:
            maximum = i
    # Пытался придумать как не проходить список два раза.
    # Но понял, что на это уйдёт чуть больше времени, чем планировал, поэтому оставил так.
    for i in range(len(_list)):
        if _list[i] == minimum:
            _list[i] = maximum
            continue
        if _list[i] == maximum:
            _list[i] = minimum
            continue

    _list.append(minimum)

    return _list


if __name__ == "__main__":
    print(sort_list([]))            # => []
    print(sort_list([2, 4, 6, 8]))  # => [8, 4, 6, 2, 2]
    print(sort_list([1]))           # => [1, 1]
    print(sort_list([1, 2, 1, 3]))  # => [3, 2, 3, 1, 1]
