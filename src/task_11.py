"""
Реализуйте класс Dessert c геттерами и сеттерами name и calories, конструктором,
принимающим на вход name и calories (не обязательные параметры), а также двумя
методами is_healthy (возвращает true при условии калорийности десерта менее
200) и is_delicious (возвращает true для всех десертов).
"""


class Dessert:

    def __init__(self, name = "", calories = 0):
        self.__name = name
        self.__calories = calories

    def is_healthy(self):
        if self.__calories < 200:
            return True
        return False

    def is_delicious(self):
        if isinstance(self, Dessert):
            return True
        return False

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value: str):
        self.__name = value

    @property
    def calories(self):
        return self.__calories

    @calories.setter
    def calories(self, value: int):
        if value > 0:
            self.__calories = value
        else:
            raise ValueError("Must be positive")


if __name__ == "__main__":
    foo = Dessert()
    print("Desert:", foo.name)
    print(foo.is_healthy())                 # => True
    print(foo.is_delicious(), '\n')         # => True

    cake = Dessert(name="Napoleon")
    print("Desert:", cake.name)
    print(cake.is_healthy())                # => True
    print(cake.is_delicious(), '\n')        # => True

    chocolate = Dessert(name="Milka", calories=500)
    print("Desert:", chocolate.name)
    print(chocolate.is_healthy())           # => False
    print(chocolate.is_delicious(), '\n')   # => True
