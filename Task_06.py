# адание №6
# Доработайте прошлую задачу.
# Добавьте сравнение прямоугольников по площади
# Должны работать все шесть операций сравнения

# @total_ordering
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

    def __eq__(self, other):
        if isinstance(other, Rectangle):
            return self.get_square() == other.get_square()
        return NotImplemented

    def __gt__(self, other):
        if isinstance(other, Rectangle):
            return self.get_square() > other.get_square()
        return NotImplemented

    def __ge__(self, other):
        if isinstance(other, Rectangle):
            return self.get_square() >= other.get_square()
        return NotImplemented

rectangle1 = Rectangle(3)
print(f'{rectangle1=}')

rectangle2 = Rectangle(2,3)
print(f'{rectangle2=}')

rectangle3 = rectangle1 + rectangle2
print(rectangle3)

rectangle4 = rectangle1 - rectangle2
print(rectangle4)

print(rectangle1>rectangle2)
print(rectangle1<rectangle2)
print(rectangle1>=rectangle2)
print(rectangle1<=rectangle2)
print(rectangle1==rectangle2)
print(rectangle1!=rectangle2)
