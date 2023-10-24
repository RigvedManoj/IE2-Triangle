import unittest
from isTriangle import Triangle


# import sys
# sys.path.append("..")
# from src.Triangle import Triangle

class StatementCoverage(unittest.TestCase):
    def testEquilateral(self):
        actual = Triangle.classify(5, 5, 5)
        expected = Triangle.Type.EQUILATERAL
        self.assertEqual(actual, expected)

    def testIsosceles1(self):
        actual = Triangle.classify(9, 5, 5)
        expected = Triangle.Type.ISOSCELES
        self.assertEqual(actual, expected)

    def testIsosceles2(self):
        actual = Triangle.classify(7, 8, 7)
        expected = Triangle.Type.ISOSCELES
        self.assertEqual(actual, expected)

    def testIsosceles3(self):
        actual = Triangle.classify(6, 6, 11)
        expected = Triangle.Type.ISOSCELES
        self.assertEqual(actual, expected)

    def testScalene(self):
        actual = Triangle.classify(9, 5, 6)
        expected = Triangle.Type.SCALENE
        self.assertEqual(actual, expected)

    def testInvalid1(self):
        actual = Triangle.classify(0, 6, 11)
        expected = Triangle.Type.INVALID
        self.assertEqual(actual, expected)

    def testInvalid2(self):
        actual = Triangle.classify(6, 6, 13)
        expected = Triangle.Type.INVALID
        self.assertEqual(actual, expected)

    def testInvalid3(self):
        actual = Triangle.classify(6, 5, 12)
        expected = Triangle.Type.INVALID
        self.assertEqual(actual, expected)


if __name__ == '__main__':
    unittest.main()
