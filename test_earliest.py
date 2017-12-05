import unittest
import get_earliest from earliest

class TestEarliest(unittest.TestCase):

    def test_same_year_and_day_diff_month(self):
        self.assertEqual(get_earliest("2/1/2016", "6/1/2016"), "2/1/2016")

if __name__ == '__main__':
    unittest.main()