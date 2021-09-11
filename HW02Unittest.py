import unittest
from HW_01 import classify_triangle

class TestStringMethods(unittest.TestCase):

    def test_classify_triangle_right(self):
        self.assertEqual(classify_triangle(3,4,5),'Right')

    def test_classify_triangle_scalene(self):
        self.assertEqual(classify_triangle(3,4,6),'Scalene')

    def test_classify_triangle_isosceles(self):
        self.assertEqual(classify_triangle(3,3,6),'Isosceles')

    def test_classify_triangle_equivilateral(self):
        self.assertEqual(classify_triangle(3,3,3),'Equilateral')



if __name__ == '__main__':
    unittest.main()