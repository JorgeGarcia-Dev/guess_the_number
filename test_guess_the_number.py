import unittest

from main import guess_the_number

class TestNumber(unittest.TestCase):
    def setUp(self):
        self.number = 5
        
    def test_guess_the_number(self):
        self.assertEqual(guess_the_number(self.number), 5)
        
if __name__ == "__main__":
    unittest.main()