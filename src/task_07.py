"""
Анаграмма — литературный приём, состоящий в перестановке букв или звуков
определённого слова (или словосочетания), что в результате даёт другое слово
или словосочетание.
Разработайте метод combine_anagrams(words_array), который принимает на вход
массив слов и разбивает их в группы по анаграммам, регистр букв не имеет
значения при определении анаграмм.
"""

def combine_anagrams(words_array: list):
    _dict = {}
    for word in words_array:
        key = "".join(sorted(word.lower()))
        if not _dict.get(key):
            _dict[key] = []
        _dict.get(key).append(word.lower())
    anagrams = []
    for array in _dict.values():
        anagrams.append(array)

    return anagrams


if __name__ == "__main__":
    print(combine_anagrams(["Cars", "For", "Potatoes", "Racs", "Four", "Scar", "Creams", "Scream"]))
    # => [['cars', 'racs', 'scar'], ['for'], ['potatoes'], ['four'], ['creams', 'scream']]
