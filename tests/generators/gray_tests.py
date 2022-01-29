import unittest

from mutwo import common_generators


class GrayTest(unittest.TestCase):
    def test_reflected_binary_code(self):
        code0 = ((0, 0),)
        code1 = ((0, 0), (0, 1), (1, 1), (1, 0))
        code2 = ((0, 0), (0, 1), (0, 2), (1, 2), (1, 1), (1, 0), (2, 0), (2, 1), (2, 2))
        code3 = (
            (0, 0, 0),
            (0, 0, 1),
            (0, 1, 1),
            (0, 1, 0),
            (1, 1, 0),
            (1, 1, 1),
            (1, 0, 1),
            (1, 0, 0),
        )

        self.assertEqual(common_generators.reflected_binary_code(2, 1), code0)
        self.assertEqual(common_generators.reflected_binary_code(2, 2), code1)
        self.assertEqual(common_generators.reflected_binary_code(2, 3), code2)
        self.assertEqual(common_generators.reflected_binary_code(3, 2), code3)


if __name__ == "__main__":
    unittest.main()
