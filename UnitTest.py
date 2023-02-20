import unittest
import math
from Project1 import waterPitcher


class Test(unittest.TestCase):
    def test1(self):
        """
        Test impossible scenario with 1 water jug.
        """
        path, q = waterPitcher(143, [math.inf, 2])
        print(q)
        self.assertEqual(path, -1, "Expected: -1")

    def test2(self):
        """
        Test impossible scenario with 1 water jug.
        """
        path, q = waterPitcher(6, [math.inf, 2])
        print(q)
        self.assertEqual(path, 6, "Expected: 6")

    def test3(self):
        """
        Test impossible scenario with two water jugs.
        """
        path, q = waterPitcher(2, [math.inf, 3, 6])
        print(q)
        self.assertEqual(path, -1, "Expected: -1")

    def test4(self):
        """
        2 water jugs without pouring between jugs.
        """
        path, q = waterPitcher(13, [math.inf, 5, 8])
        print(q)
        self.assertEqual(path, 4, "Expected: 4")

    def test5(self):
        """
        2 water jugs with pouring between jugs.
        """
        path, q = waterPitcher(2, [math.inf, 5, 8])
        print(q)
        self.assertEqual(path, 5, "Expected: 5")

    def test6(self):
        """
        3 water jugs without pouring between jugs result.
        """
        path, q = waterPitcher(68, [math.inf, 5, 8, 11])
        print(q)
        self.assertEqual(path, 14, "Expected: 14")

    def test7(self):
        """
        3 water jugs with pouring between jugs result.
        """
        path, q = waterPitcher(2, [math.inf, 4, 7, 11])
        print(q)
        self.assertEqual(path, 9, "Expected: 9")

    def test8(self):
        """
        4 water jugs without pouring between jugs result.
        """
        path, q = waterPitcher(151, [math.inf, 2, 5, 6, 73])
        print(q)
        self.assertEqual(path, 6, "Expected: 6")

    def test9(self):
        """
        4 water jugs with pouring between jugs result.
        """
        path, q = waterPitcher(143, [math.inf, 2, 5, 6, 73])
        print(q)
        self.assertEqual(path, 7, "Expected: 7")

    def test10(self):
        """
        5 water jugs with pouring between jugs result.
        """
        path, q = waterPitcher(181, [math.inf, 1, 4, 10, 15, 22])
        print(q)
        self.assertEqual(path, 19, "Expected: 19")

    def test11(self):
        """
        6 water jugs with pouring between jugs result.
        """
        path, q = waterPitcher(11443, [math.inf, 2, 3, 5, 19, 121, 852])
        print(q)
        self.assertEqual(path, 36, "Expected: 36")


def unitTest():
    unitTest = unittest.TestSuite()

    # TestSuite represents an aggregation of individual test cases
    for i in range(11):
        name = 'test' + str(i + 1)

        unitTest.addTest(Test(name))

    return unitTest


if __name__ == '__main__':
    runner = unittest.TextTestRunner()
    runner.run(unitTest())
