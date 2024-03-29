# Задание №2
# Создайте класс Архив, который хранит пару свойств.
# Например, число и строку.
# При нового экземпляра класса, старые данные из ранее
# созданных экземпляров сохраняются в пару списковархивов
# list-архивы также являются свойствами экземпляра

class Archiv:
    _instance = None

    def __new__(cls, string, number):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance._string_archive = []
            cls._instance._number_archive = []
        else:
            cls._instance._string_archive.append(cls._instance.string)
            cls._instance._number_archive.append(cls._instance.number)

        return cls.instance

    def __str__(self):
        return f'{self._number, self.string}'

    def __init__(self, string, number):
        self.string = string
        self.number = number

    def string_archive(self):
        return self._string_archive

    def number_archive(self):
        return self._number_archive

first = Archiv('a',1)
second = Archiv('b',2)
print(first, second)
print(first.string_archive(), first.number_archive())

third = Archiv('c',3)
print(third.string_archive(), third.number_archive())

print(third)