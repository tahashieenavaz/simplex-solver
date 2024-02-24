import unittest


class TestSimplexSolver(unittest.TestCase):
    def test_failing_equal(self):
        self.assertEqual(3, 2)

    def test_passing_equal(self):
        self.assertEqual(3, 3)


if __name__ == "__main__":
    unittest.main()
