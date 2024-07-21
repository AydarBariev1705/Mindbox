import unittest

from taks1.shapes import Circle, Triangle


class TestCircle(unittest.TestCase):
    def test_area(self):
        circle = Circle(2)
        self.assertAlmostEqual(circle.area(), 4 * 3.141592653589793, places=5)

    def test_is_right_angle(self):
        circle = Circle(2)
        self.assertFalse(circle.is_right_angle())


class TestTriangle(unittest.TestCase):
    def test_area(self):
        triangle = Triangle(3, 4, 5)
        self.assertAlmostEqual(triangle.area(), 6.0)

    def test_is_right_angle(self):
        triangle = Triangle(3, 4, 5)
        self.assertTrue(triangle.is_right_angle())

    def test_non_right_triangle(self):
        triangle = Triangle(5, 5, 8)
        self.assertFalse(triangle.is_right_angle())

    def test_invalid_triangle(self):
        with self.assertRaises(ValueError):
            Triangle(1, 2, 3)


if __name__ == '__main__':
    unittest.main()
