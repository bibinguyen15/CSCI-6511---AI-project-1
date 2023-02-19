import unittest
import math
from Project1 import waterPitcher


class Test(unittest.TestCase):
    def test1(self):
        """
        Test impossible scenario with 1 water jug.
        """
        path = waterPitcher(143, [math.inf, 2])
        self.assertEqual(path, -1, "-1")

    def test2(self):
        """
        Test impossible scenario with 1 water jug.
        """
        path = waterPitcher(6, [math.inf, 2])
        self.assertEqual(path, 6, "6")

    def test3(self):
        """
        Test impossible scenario with two water jugs.
        """
        path = waterPitcher(2, [math.inf, 3, 6])
        self.assertEqual(path, -1, "-1")

    def test4(self):
        """
        2 water jugs without pouring between jugs.
        """
        path = waterPitcher(13, [math.inf, 5, 8])
        self.assertEqual(path, 4, "4")

    def test5(self):
        """
        2 water jugs with pouring between jugs.
        """
        path = waterPitcher(2, [math.inf, 5, 8])
        self.assertEqual(path, 5, "5")

    def test6(self):
        """
        3 water jugs without pouring between jugs result.
        """
        path = waterPitcher(68, [math.inf, 5, 8, 11])
        self.assertEqual(path, 14, "14")

    def test7(self):
        """
        3 water jugs with pouring between jugs result.
        """
        path = waterPitcher(2, [math.inf, 4, 7, 11])
        self.assertEqual(path, 9, "9")

    def test8(self):
        """
        4 water jugs without pouring between jugs result.
        """
        path = waterPitcher(151, [math.inf, 2, 5, 6, 73])
        self.assertEqual(path, 6, "6")

    def test9(self):
        """
        4 water jugs with pouring between jugs result.
        """
        path = waterPitcher(143, [math.inf, 2, 5, 6, 73])
        self.assertEqual(path, 7, "7")

    def test10(self):
        """
        5 water jugs with pouring between jugs result.
        """
        path = waterPitcher(27, [math.inf, 1, 4, 10, 15, 22])
        self.assertEqual(path, 5, "5")


def unitTest():
    unitTest = unittest.TestSuite()

    # TestSuite represents an aggregation of individual test cases
    for i in range(10):
        name = 'test' + str(i + 1)

        unitTest.addTest(Test(name))

    return unitTest


if __name__ == '__main__':
    runner = unittest.TextTestRunner()
    runner.run(unitTest())
