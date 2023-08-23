# Задание №5
# Дорабатываем класс прямоугольник из прошлого семинара.
# Добавьте возможность сложения и вычитания.
# При этом должен создаваться новый экземпляр
# прямоугольника.
# Складываем и вычитаем периметры, а не длинну и ширину.
# При вычитании не допускайте отрицательных значений.

# Задание №2
# Создайте класс прямоугольник.
# Класс должен принимать длину и ширину при создании
# экземпляра.
# У класса должно быть два метода, возвращающие периметр
# и площадь.
# Если при создании экземпляра передаётся только одна
# сторона, считаем что у нас квадрат.

class Rectangle():

    def __add__(self, other):
        if isinstance(other, Rectangle):
            return Rectangle(self.a + other.a, self.b+other.b)
        return NotImplemented

    def __init__(self, a, b=None):
        self.a = a
        if b is None:
            self.b = a
        else:
            self.b = b

    def get_square(self):
        return self.a * self.b

    def get_length(self):
        return 2 * (self.a + self.b)

    def __repr__(self):
        return f"Rectangle({self.a}, {self.b})"

    def __sub__(self, other):
        if isinstance(other, Rectangle):
            if other.a > self.a or other.b > self.b:
                raise ValueError("Ошибка!")
            return Rectangle(self.a - other.a, self.b-other.b)


rectangle1 = Rectangle(3)
print(rectangle1)

rectangle2 = Rectangle(2,3)
print(rectangle2)

rectangle3 = rectangle1 + rectangle2
print(rectangle3)

rectangle4 = rectangle2 - rectangle1
print(rectangle4)


