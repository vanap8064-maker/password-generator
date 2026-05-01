import unittest
from src.logic import generate_password

class TestGenerator(unittest.TestCase):
    def test_length(self):
        pwd = generate_password(10, True, True, False)
        self.assertEqual(len(pwd), 10)

    def test_no_options(self):
        with self.assertRaises(ValueError):
            generate_password(10, False, False, False)