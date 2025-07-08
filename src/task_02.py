"""
Дан список list и числовой диапазон range. Разработайте метод coincidence(list,
range) для определения элементов из массива list, значения которого входят в
указанный диапазон range. Если не передан хотя бы один из параметров, то
должен вернуться пустой массив.
"""

def coincidence(_list=None, _range=None):
    if _list is None or _range is None:
        return []
    ans = []
    for i in _list:
        if isinstance(i, float):
            if float(_range[0]) <= i <= float(_range[-1]):
                ans.append(i)
                continue
        if i in _range:
            ans.append(i)

    return ans


if __name__ == "__main__":
    print(coincidence([1, 2, 3, 4, 5], range(3, 6)))                # => [3, 4, 5]
    print(coincidence())                                                 # => []
    print(coincidence([None, 1, 'foo', 4, 2, 2.5], range(1, 4)))    # => [1, 2, 2.5]
