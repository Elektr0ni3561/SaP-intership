"""
Разработать метод date_in_future(integer), который вернет дату через integer дней.
Если integer не является целым числом, то метод должен вывести текущую дату.
Формат возвращаемой методом даты должен иметь следующий вид '24-03-2001
22:33:44'.
"""

from datetime import datetime, timedelta

DATE_PATTERN = "%d-%m-%Y %H:%M:%S"


def date_in_future(integer):
    if not isinstance(integer, int):
        print(datetime.today().strftime(DATE_PATTERN))
        return

    print((datetime.today() + timedelta(days=integer)).strftime(DATE_PATTERN))


if __name__ == "__main__":
    date_in_future([])  # => текущая дата
    date_in_future(2)   # => текущая дата + 2 дня
