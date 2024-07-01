import unittest
from just_commit.main import main

class TestMainFunctionality(unittest.TestCase):
    def test_main_output(self):
        self.assertIsNone(main(), "The main function should return None")

if __name__ == '__main__':
    unittest.main()
