import unittest

import ranges  # type: ignore

from mutwo import core_events
from mutwo import common_generators


class TendencyTest(unittest.TestCase):
    def setUp(self):
        minima_curve = core_events.Envelope([(0, 0), (1, 1), (2, 0)])
        maxima_curve = core_events.Envelope([(0, 1), (1, 2), (2, 3)])
        self.tendency = common_generators.Tendency(minima_curve, maxima_curve)

    def test_range_at(self):
        self.assertEqual(self.tendency.range_at(-100), ranges.Range(0, 1))
        self.assertEqual(self.tendency.range_at(0), ranges.Range(0, 1))
        self.assertEqual(self.tendency.range_at(1), ranges.Range(1, 2))
        self.assertEqual(self.tendency.range_at(2), ranges.Range(0, 3))
        self.assertEqual(self.tendency.range_at(100), ranges.Range(0, 3))

    def test_gamble_at(self):
        for position in (-100, 0, 1, 2, 100):
            value = self.tendency.value_at(position)
            current_range = self.tendency.range_at(position)
            self.assertGreaterEqual(value, current_range.start)
            self.assertLessEqual(value, current_range.end)


if __name__ == "__main__":
    unittest.main()
