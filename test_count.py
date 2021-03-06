import unittest


from count_soln1 import count_words


class CountWordsTests(unittest.TestCase):

    """Tests for count_words."""

    def test_simple_sentence(self):
        actual = count_words("OH what a day what a lovely day")
        expected = {'oh': 1, 'what': 2, 'a': 2, 'day': 2, 'lovely': 1}
        self.assertEqual(actual, expected)

    def test_apostrophe(self):
        actual = count_words("don't stop believing")
        expected = {"don't": 1, 'stop': 1, 'believing': 1}
        self.assertEqual(actual, expected)

    # To test the Bonus part of this exercise, comment out the following line
    # @unittest.expectedFailure
    def test_capitalization(self):
        actual = count_words("Oh what a day what a lovely day")
        expected = {'oh': 1, 'what': 2, 'a': 2, 'day': 2, 'lovely': 1}
        self.assertEqual(actual, expected)

    # To test the Bonus part of this exercise, comment out the following line
    # @unittest.expectedFailure
    def test_symbols(self):
        actual = count_words("Oh what a day, what a lovely day!")
        expected = {'oh': 1, 'what': 2, 'a': 2, 'day': 2, 'lovely': 1}
        self.assertEqual(actual, expected)


if __name__ == "__main__":
    unittest.main()