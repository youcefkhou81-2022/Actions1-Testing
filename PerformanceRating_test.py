import unittest
from PerformanceRating import PerformanceRating

class TestPerformanceRating(unittest.TestCase):

    # Equivalence Classes:
    # EC1: time < 0
    def test_t1(self):
        pr = PerformanceRating()
        self.assertEqual(pr.rate(-5, True), "ERROR")

    # EC2: 0 <= time <= 12
    def test_t2(self):
        pr = PerformanceRating()
        self.assertEqual(pr.rate(5, False), 80)

    # EC3: 13 <= time <= 20
    def test_t3(self):
        pr = PerformanceRating()
        self.assertEqual(pr.rate(15, False), 50)

    # EC4: 20 <= time <= 60 
    def test_t4(self):
        pr = PerformanceRating()
        self.assertEqual(pr.rate(30, False), 20)

    # EC5: time > 60
    def test_t5(self):
        pr = PerformanceRating()
        self.assertEqual(pr.rate(100, False), "ERROR")

    # Boundary Values:
    # BV1: time = -inf
    def test_t6(self):
        pr = PerformanceRating()
        self.assertEqual(pr.rate(float("-inf"), True), "ERROR")

    # BV2: time = -1
    def test_t7(self):
        pr = PerformanceRating()
        self.assertEqual(pr.rate(-1, False), "ERROR")

    # BV3: time = 0
    def test_t8(self):
        pr = PerformanceRating()
        self.assertEqual(pr.rate(0, False), 80)

    # BV4: time = 12
    def test_t9(self):
        pr = PerformanceRating()
        self.assertEqual(pr.rate(12, False), 80)

    # BV5: time = 13
    def test_t10(self):
        pr = PerformanceRating()
        self.assertEqual(pr.rate(13, False), 50)

    # BV6: time = 20
    def test_t11(self):
        pr = PerformanceRating()
        self.assertEqual(pr.rate(20, False), 50)

    # BV7: time = 21
    def test_t12(self):
        pr = PerformanceRating()
        self.assertEqual(pr.rate(21, False), 20)

    # BV8: time = 60
    def test_t13(self):
        pr = PerformanceRating()
        self.assertEqual(pr.rate(60, False), 20)

    # BV9: time = 61
    def test_t14(self):
        pr = PerformanceRating()
        self.assertEqual(pr.rate(61, True), "ERROR")

    # BV10: time = +inf
    def test_t15(self):
        pr = PerformanceRating()
        self.assertEqual(pr.rate(float("inf"), False), "ERROR")

    # # Decision Table Testing:
    # def test_t16(self):