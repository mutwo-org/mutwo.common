import unittest

from mutwo import common_generators


class EdwardsTest(unittest.TestCase):
    def test_activity_level(self):
        activity_level0 = common_generators.ActivityLevel()
        activity_level1 = common_generators.ActivityLevel(start_at=1)

        for activity_level, start_at in (
            (activity_level0, 0),
            (activity_level1, 1),
        ):
            for level in range(9):
                level += 1
                states = common_generators.constants.ACTIVITY_LEVEL_TUPLE[level][
                    start_at
                ]
                for nth_iteration in range(10):
                    self.assertEqual(bool(states[nth_iteration]), activity_level(level))

        # test invalid values for start_at
        self.assertRaises(
            ValueError, lambda: common_generators.ActivityLevel(start_at=3)
        )
        self.assertRaises(
            ValueError, lambda: common_generators.ActivityLevel(start_at=-1)
        )


if __name__ == "__main__":
    unittest.main()
