# Написать метод multiply_numbers(inputs), который вернет произведение цифр,
# входящих в inputs.

import re

def multiply_numbers(*inputs):
# Использую *, потому что в первом варианте ничего не передаётся и иначе будет ошибка.
    ans = None
    for arg in inputs:
        numbers = re.findall(r"[\d]", str(arg))
        for item in numbers:
            if not ans:
                ans = int(item)
                continue
            ans *= int(item)
    return ans

if __name__ == "__main__":
    print(multiply_numbers())           # => None
    print(multiply_numbers('ss'))       # => None
    print(multiply_numbers('1234'))     # => 24
    print(multiply_numbers('sssdd34'))  # => 12
    print(multiply_numbers(2.3))        # => 6
    print(multiply_numbers([5, 6, 4]))  # => 120
