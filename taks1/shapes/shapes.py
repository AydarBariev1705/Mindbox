from abc import ABC, abstractmethod
import math


class Shape(ABC):
    @abstractmethod
    def area(self) -> float:
        """
        Вычислить площадь фигуры
        """
        pass

    @abstractmethod
    def is_right_angle(self) -> bool:
        """
        Проверить, является ли фигура прямоугольной (только для треугольников)
        """
        pass


class Circle(Shape):
    def __init__(self, radius: float):
        if radius <= 0:  # Проверка чтобы радиус круга был больше нуля
            raise ValueError('Радиус круга должны быть > 0!')
        self.radius = radius

    def area(self) -> float:
        # Вычисляем площадь у круга
        return math.pi * (self.radius ** 2)

    def is_right_angle(self) -> bool:
        # У Круга углов нет
        return False


class Triangle(Shape):
    def __init__(self, a: float, b: float, c: float):
        if a <= 0 or b <= 0 or c <= 0:  # Проверка чтобы стороны треугольника были больше нуля
            raise ValueError('Стороны треугольника должны быть > 0!')
        if a + b <= c or a + c <= b or b + c <= a:  # Проверка для возможности сформировать треугольник
            raise ValueError('Одна сторона треугольника должна быть больше или равна сумме двух других сторон!')
        self.a = a
        self.b = b
        self.c = c

    def area(self) -> float:
        """
        Вычислить площадь треугольника
        """
        hp = (self.a + self.b + self.c) / 2  # hp - half perimetr (половина периметра треугольника)

        return math.sqrt(hp * (hp - self.a) * (hp - self.b) * (hp - self.c))

    def is_right_angle(self) -> bool:
        """
        Определяем прямоугольный ли треугольник
        """
        sides = sorted([self.a, self.b, self.c])  # Самая длинная сторона это гипотенуза (sides[2])
        return math.isclose(sides[0] ** 2 + sides[1] ** 2, sides[2] ** 2)
