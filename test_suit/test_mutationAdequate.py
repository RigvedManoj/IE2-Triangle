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

    def testInvalid4(self):
        actual = Triangle.classify(6, 6, 13)
        expected = Triangle.Type.INVALID
        self.assertEqual(actual, expected)

    def testInvalid5(self):
        actual = Triangle.classify(6, 5, 12)
        expected = Triangle.Type.INVALID
        self.assertEqual(actual, expected)

    def testMutation1(self):
        actual = Triangle.classify(6, 12, 6)
        expected = Triangle.Type.INVALID
        self.assertEqual(actual, expected)

    def testMutation2(self):
        actual = Triangle.classify(12, 6, 6)
        expected = Triangle.Type.INVALID
        self.assertEqual(actual, expected)

    def testMutation3(self):
        actual = Triangle.classify(6, 6, 12)
        expected = Triangle.Type.INVALID
        self.assertEqual(actual, expected)

    def testMutation4(self):
        actual = Triangle.classify(4, 5, 9)
        expected = Triangle.Type.INVALID
        self.assertEqual(actual, expected)

    def testMutation5(self):
        actual = Triangle.classify(9, 5, 4)
        expected = Triangle.Type.INVALID
        self.assertEqual(actual, expected)

    def testMutation6(self):
        actual = Triangle.classify(4, 9, 5)
        expected = Triangle.Type.INVALID
        self.assertEqual(actual, expected)

    def testMutation7(self):
        actual = Triangle.classify(-1, 3, 3)
        expected = Triangle.Type.INVALID
        self.assertEqual(actual, expected)

    def testMutation8(self):
        actual = Triangle.classify(3, -1, 3)
        expected = Triangle.Type.INVALID
        self.assertEqual(actual, expected)

    def testMutation9(self):
        actual = Triangle.classify(3, 3, -1)
        expected = Triangle.Type.INVALID
        self.assertEqual(actual, expected)

    def testMutation10(self):
        actual = Triangle.classify(0, 3, 3)
        expected = Triangle.Type.INVALID
        self.assertEqual(actual, expected)

    def testMutation11(self):
        actual = Triangle.classify(3, 0, 3)
        expected = Triangle.Type.INVALID
        self.assertEqual(actual, expected)

    def testMutation12(self):
        actual = Triangle.classify(3, 3, 0)
        expected = Triangle.Type.INVALID
        self.assertEqual(actual, expected)


if __name__ == '__main__':
    unittest.main()
