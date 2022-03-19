import itertools
import unittest

from mutwo import common_generators


class IndexBasedBacktrackingTest(unittest.TestCase):
    class QueenProblem8(common_generators.IndexBasedBacktracking):
        queen_count = 8
        point_list = list(
            itertools.combinations_with_replacement(range(queen_count), 2)
        )
        point_list.extend(
            [tuple(reversed(point)) for point in point_list if len(set(point)) == 2]
        )

        def element_index_to_item_sequence(self, element_index, element_list):
            return self.point_list

        @property
        def solution_count(self):
            return self.queen_count

        def is_valid(self, element_list):
            solution = self.element_list_to_solution(element_list)
            for queen0, queen1 in itertools.combinations(solution, 2):
                # x != x, y != y
                is_valid = all(
                    value0 != value1 for value0, value1 in zip(queen0, queen1)
                )
                difference_x, difference_y = (
                    value0 - value1 for value0, value1 in zip(queen0, queen1)
                )
                is_valid = is_valid and (difference_x != difference_y)
                if not is_valid:
                    return False
            return True

    def test_solve(self):
        queen_problem_8 = self.QueenProblem8()
        self.assertEqual(
            queen_problem_8.solve(),
            ((0, 0), (1, 2), (2, 5), (3, 7), (4, 6), (6, 1), (5, 3), (7, 4)),
        )


if __name__ == "__main__":
    unittest.main()
