# Разработайте функцию count_words(string), которая будет возвращать словарь со
# статистикой частоты употребления входящих в неё слов.

import re

def count_words(string):
    word_frequency = {}
    for word in re.findall(r"\w+", string.lower()):
        if word in word_frequency:
            word_frequency[word] += 1
            continue
        word_frequency[word] = 1

    return word_frequency

if __name__ == "__main__":
    print(count_words("A man, a plan, a canal -- Panama")) # => {"a": 3, "man": 1, "canal": 1, "panama": 1, "plan": 1}
    print(count_words("Doo bee doo bee doo"))              # => {"doo": 3, "bee": 2}