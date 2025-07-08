"""
Разработайте метод is_palindrome(string), который будет определять, является ли
параметр string палиндромом (строкой, которая читается одинаково как сначала
так и с конца), при условии игнорирования пробелов, знаков препинания и
регистра.
"""

import re


def is_palindrome(text):
    if text is None:
        return False
    sub_string = re.sub(r"[^a-zA-Zа-яА-Я\d]", "", str(text))
    sub_string = sub_string.lower()
    for i in range(len(sub_string) // 2):
        if sub_string[i] != sub_string[-i - 1]:
            return False

    return True


if __name__ == "__main__":
    print(is_palindrome("A man, a plan, a canal -- Panama"))    # => True
    print(is_palindrome("Madam, I'm Adam!"))                    # => True
    print(is_palindrome(333))                                   # => True
    print(is_palindrome(None))                                  # => False
    print(is_palindrome("Abracadabra"))                         # => False
