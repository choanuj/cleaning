import unittest
from cleaner import Cleaner

class TestCleaner(unittest.TestCase):
    def setUp(self):
        self.cleaner = Cleaner()

    def test_remove_punctuation(self):
        text = "Hello, world! How are you?"
        result = self.cleaner.remove_punctuation(text)
        expected = "Hello world How are you"
        self.assertEqual(result, expected)
        self.assertEqual(self.cleaner.remove_punctuation(""), "")
        self.assertEqual(self.cleaner.remove_punctuation(123), "")

    def test_remove_stop_words(self):
        text = "The cat is on the mat"
        result = self.cleaner.remove_stop_words(text)
        expected = "cat mat"
        self.assertEqual(result, expected)
        self.assertEqual(self.cleaner.remove_stop_words(""), "")
        self.assertEqual(self.cleaner.remove_stop_words(123), "")

    def test_lowercase(self):
        text = "Hello WORLD"
        result = self.cleaner.lowercase(text)
        expected = "hello world"
        self.assertEqual(result, expected)
        self.assertEqual(self.cleaner.lowercase(""), "")
        self.assertEqual(self.cleaner.lowercase(123), "")

    def test_remove_numbers(self):
        text = "I have 2 cats and 3 dogs"
        result = self.cleaner.remove_numbers(text)
        expected = "I have  cats and  dogs"
        self.assertEqual(result, expected)
        self.assertEqual(self.cleaner.remove_numbers(""), "")
        self.assertEqual(self.cleaner.remove_numbers(123), "")

    def test_normalize_whitespace(self):
        text = "  Hello   world  "
        result = self.cleaner.normalize_whitespace(text)
        expected = "Hello world"
        self.assertEqual(result, expected)
        self.assertEqual(self.cleaner.normalize_whitespace(""), "")
        self.assertEqual(self.cleaner.normalize_whitespace(123), "")

    def test_remove_special_characters(self):
        text = "Hello @world! 😊"
        result = self.cleaner.remove_special_characters(text)
        expected = "Hello world"
        self.assertEqual(result, expected)
        self.assertEqual(self.cleaner.remove_special_characters(""), "")
        self.assertEqual(self.cleaner.remove_special_characters(123), "")

    def test_remove_html_tags(self):
        text = "<p>Hello <b>world</b>!</p>"
        result = self.cleaner.remove_html_tags(text)
        expected = "Hello world!"
        self.assertEqual(result, expected)
        self.assertEqual(self.cleaner.remove_html_tags(""), "")
        self.assertEqual(self.cleaner.remove_html_tags(123), "")

    def test_remove_urls_emails(self):
        text = "Visit http://example.com or test@domain.com"
        result = self.cleaner.remove_urls_emails(text)
        expected = "Visit or"
        self.assertEqual(result, expected)
        self.assertEqual(self.cleaner.remove_urls_emails(""), "")
        self.assertEqual(self.cleaner.remove_urls_emails(123), "")

    def test_clean_all(self):
        text = "  The <b>Cat</b> is 123 @on the http://example.com mat!!!  "
        result = self.cleaner.clean_all(text)
        expected = "cat mat"
        self.assertEqual(result, expected)
        self.assertEqual(self.cleaner.clean_all(""), "")
        self.assertEqual(self.cleaner.clean_all(123), "")

if __name__ == '__main__':
    unittest.main()