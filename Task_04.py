# Задание №3
# Добавьте к задачам 1 и 2 строки документации для классов.

# Задание №2
# Создайте класс Архив, который хранит пару свойств.
# Например, число и строку.
# При нового экземпляра класса, старые данные из ранее
# созданных экземпляров сохраняются в пару списковархивов
# list-архивы также являются свойствами экземпляра

class Archiv:
    """Это класс  """
    _instance = None

    def __new__(cls, string, number):
        """
        Это создание класса
        :param string:
        :param number:
        """
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance._string_archive = []
            cls._instance._number_archive = []
        else:
            cls._instance._string_archive.append(cls._instance.string)
            cls._instance._number_archive.append(cls._instance.number)

        return cls._instance

    def __str__(self):
        """
        print
        :return:
        """
        return f'{self.number, self.string}'

    def __init__(self, string, number):
        """
        Создание экземпляра класса
        :param string:
        :param number:
        """
        self.string = string
        self.number = number

    def string_archive(self):
        """
        Архивация строк
        :return:
        """
        return self._string_archive

    def number_archive(self):
        """
        Архивация цифр
        :return:
        """
        return self._number_archive

    def __repr__(self):
        """
        Для разработчика
        :return:
        """
        return f'Archive("{self.string}", {self.number})'



first = Archiv('a',1)
second = Archiv('b',2)
print(first, second)
print(first.string_archive(), first.number_archive())

third = Archiv('c',3)
print(third.string_archive(), third.number_archive())

print(third)
print(third.__repr__())

print(my_list := [first, second,  third])

for item in my_list:
    print(item)
