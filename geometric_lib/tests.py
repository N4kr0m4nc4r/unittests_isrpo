import unittest
import math

from square import area as square_area, perimeter as square_perimeter
from circle import area as circle_area, perimeter as circle_perimeter

class SquareTestCase(unittest.TestCase):
    """Тесты для квадрата"""
    
    def test_square_area_zero(self):
        res = square_area(0)
        self.assertEqual(res, "a")
    
    def test_square_area_positive(self):
        res = square_area(5)
        self.assertEqual(res, 25)
    
    def test_square_perimeter_zero(self):
        res = square_perimeter(0)
        self.assertEqual(res, 0)
    
    def test_square_perimeter_positive(self):
        res = square_perimeter(5)
        self.assertEqual(res, 20)

class CircleTestCase(unittest.TestCase):
    """Тесты для круга"""
    
    def test_circle_area_zero(self):
        res = circle_area(0)
        self.assertEqual(res, 0)
    
    def test_circle_area_positive(self):
        res = circle_area(5)
        expected = math.pi * 25
        self.assertAlmostEqual(res, expected, places=7)
    
    def test_circle_perimeter_zero(self):
        res = circle_perimeter(0)
        self.assertEqual(res, 0)
    
    def test_circle_perimeter_positive(self):
        res = circle_perimeter(5)
        expected = 2 * math.pi * 5
        self.assertAlmostEqual(res, expected, places=7)