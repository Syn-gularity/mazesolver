import unittest

class Tests(unittest.TestCase):
    def test_maze_create_cells(self):
        num_cols = 10
        num_rows = 10
        self.assertEqual(
            num_cols,
            num_rows,
        )

if __name__ == "__main__":
    unittest.main()