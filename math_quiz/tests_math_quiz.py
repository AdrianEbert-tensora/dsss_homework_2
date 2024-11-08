import unittest
from math_quiz import generate_random_integer, get_random_operator, create_math_problem


class TestMathGame(unittest.TestCase):

    def test_generate_random_integer(self):

        min_val = 1
        max_val = 10
        for _ in range(1000):  # Testing a large number of random values
            rand_num = generate_random_integer(min_val, max_val)
            self.assertTrue(min_val <= rand_num <= max_val)

    def test_get_random_operator(self):

        valid_operators = ['+', '-', '*']
        for _ in range(100):  # Testing a large number of random operators
            operator = get_random_operator()
            self.assertIn(operator, valid_operators)

    def test_create_math_problem(self):

        test_cases = [
            (5, 2, '+', '5 + 2', 7),
            (7, 3, '-', '7 - 3', 4),
            (4, 6, '*', '4 * 6', 24)
        ]

        for num1, num2, operator, expected_problem, expected_answer in test_cases:
            problem, answer = create_math_problem(num1, num2, operator)
            self.assertEqual(problem, expected_problem)
            self.assertEqual(answer, expected_answer)


if __name__ == "__main__":
    unittest.main()


    