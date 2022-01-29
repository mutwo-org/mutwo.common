import unittest

from mutwo import common_generators


class ToussaintTest(unittest.TestCase):
    def test_euclidean(self):
        rhythms = ((2, 2), (3, 2), (3, 2, 3), (4, 3, 3))
        for rhythm in rhythms:
            self.assertEqual(common_generators.euclidean(sum(rhythm), len(rhythm)), rhythm)

    def test_paradiddle(self):
        # using the examples that Toussaint provided in his paper
        self.assertEqual(common_generators.paradiddle(8), ((0, 2, 3, 5), (1, 4, 6, 7)))
        self.assertEqual(
            common_generators.paradiddle(12), ((0, 2, 4, 5, 7, 9), (1, 3, 6, 8, 10, 11))
        )
        self.assertEqual(
            common_generators.paradiddle(16),
            ((0, 2, 4, 6, 7, 9, 11, 13), (1, 3, 5, 8, 10, 12, 14, 15)),
        )

    def test_alternating_hands(self):
        # using the examples that Toussaint provided in his paper
        self.assertEqual(common_generators.alternating_hands((1, 1, 2)), ((0, 2, 5), (1, 4, 6)))
        self.assertEqual(
            common_generators.alternating_hands((1, 2, 1, 2, 2)),
            ((0, 3, 6, 9, 12), (1, 4, 8, 11, 14)),
        )


if __name__ == "__main__":
    unittest.main()
