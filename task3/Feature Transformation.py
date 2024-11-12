import math
import unittest

def time_to_cyclic_features(time):
    sin_time = math.sin(2 * math.pi * time / 24)
    cos_time = math.cos(2 * math.pi * time / 24)
    return sin_time, cos_time

def time_difference_in_hours(time1, time2):
    sin1, cos1 = time_to_cyclic_features(time1)
    sin2, cos2 = time_to_cyclic_features(time2)
    dot_product = sin1 * sin2 + cos1 * cos2
    angle = math.acos(dot_product)
    diff = (angle / (2 * math.pi)) * 24
    return diff

class TestCyclicTime(unittest.TestCase):

    def test_time_to_cyclic_features(self):
        result = time_to_cyclic_features(23)
        self.assertAlmostEqual(result[0], math.sin(2 * math.pi * 23 / 24))
        self.assertAlmostEqual(result[1], math.cos(2 * math.pi * 23 / 24))

    def test_time_difference_in_hours(self):
        self.assertAlmostEqual(time_difference_in_hours(23, 1), 2)
        self.assertAlmostEqual(time_difference_in_hours(10, 15), 5)
        self.assertAlmostEqual(time_difference_in_hours(10, 10), 0)
        self.assertAlmostEqual(time_difference_in_hours(0, 12), 12)
        self.assertAlmostEqual(time_difference_in_hours(23.5, 0.5), 1)

if __name__ == "__main__":
    unittest.main()
