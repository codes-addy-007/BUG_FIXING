%%writefile test_student_utils.py

import unittest

from student_utils import calculate_average, is_passing, get_grade


class TestStudentUtils(unittest.TestCase):

    def test_average_of_three_marks(self):
        self.assertEqual(
            calculate_average([80, 90, 100]),
            90.0
        )

    def test_average_single_mark(self):
        self.assertEqual(
            calculate_average([40]),
            40.0
        )

    def test_above_pass_mark(self):
        self.assertEqual(is_passing(41), True)

    def test_exact_pass_mark(self):
        self.assertEqual(is_passing(40), True)

    def test_below_pass_mark(self):
        self.assertEqual(is_passing(39), False)

    def test_distinction(self):
        self.assertEqual(get_grade(95), "Distinction")

    def test_first(self):
        self.assertEqual(get_grade(60), "First")

    def test_second(self):
        self.assertEqual(get_grade(45), "Second")

    def test_fail(self):
        self.assertEqual(get_grade(30), "Fail")


if __name__ == "__main__":
    unittest.main()
