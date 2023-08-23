# Задание №1
# Создайте класс Моя Строка, где:
# будут доступны все возможности str
# дополнительно хранятся имя автора строки и время создания
# (time.time)
import time
from getpass import getuser

class MyString(str):
    def __new__(cls, str_val):
        instance = super().__new__(cls,str_val)
        instance.name = getuser()
        instance.time = time.time()
        return instance

a = MyString('Hello world')
print(a, a.name, a.time)

print(a.split())
