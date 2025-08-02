import re
import string

class Cleaner:
    def __init__(self):
        # Default stop words list (hardcoded to avoid file dependency)
        self.stop_words = {
            'the', 'a', 'an', 'is', 'are', 'was', 'were', 'be', 'in', 'on',
            'at', 'to', 'and', 'but', 'or'
        }

    def remove_punctuation(self, text):
        """Remove punctuation from text."""
        if not isinstance(text, str):
            return ""
        return ''.join(c for c in text if c not in string.punctuation)

    def remove_stop_words(self, text):
        """Remove stop words from text."""
        if not isinstance(text, str):
            return ""
        words = text.split()
        return ' '.join(word for word in words if word.lower() not in self.stop_words)

    def lowercase(self, text):
        """Convert text to lowercase."""
        if not isinstance(text, str):
            return ""
        return text.lower()

    def remove_numbers(self, text):
        """Remove digits from text."""
        if not isinstance(text, str):
            return ""
        return ''.join(c for c in text if not c.isdigit())

    def normalize_whitespace(self, text):
        """Remove extra whitespace and trim leading/trailing spaces."""
        if not isinstance(text, str):
            return ""
        return ' '.join(text.split())

    def remove_special_characters(self, text):
        """Remove non-alphanumeric characters (except spaces)."""
        if not isinstance(text, str):
            return ""
        return re.sub(r'[^a-zA-Z0-9\s]', '', text).strip()

    def remove_html_tags(self, text):
        """Remove HTML tags from text."""
        if not isinstance(text, str):
            return ""
        return re.sub(r'<[^>]+>', '', text)

    def remove_urls_emails(self, text):
        """Remove URLs and email addresses from text."""
        if not isinstance(text, str):
            return ""
        # Remove URLs
        text = re.sub(r'https?://\S+|www\.\S+', '', text)
        # Remove emails
        text = re.sub(r'\b[\w\.-]+@[\w\.-]+\.\w+\b', '', text)
        return ' '.join(text.split()).strip()

    def clean_all(self, text):
        """Apply all cleaning methods in sequence."""
        if not isinstance(text, str):
            return ""
        text = self.remove_html_tags(text)
        text = self.remove_urls_emails(text)
        text = self.remove_special_characters(text)
        text = self.remove_numbers(text)
        text = self.remove_punctuation(text)
        text = self.remove_stop_words(text)
        text = self.lowercase(text)
        text = self.normalize_whitespace(text)
        return text

if __name__ == "__main__":
    cleaner = Cleaner()

    # Example text
    text = "  Hello, World! Visit http://example.com or email test@domain.com. The 123 cats are <b>RUNNING</b>!!!  "

    # Test each cleaning method
    print("Original:", text)
    print("Remove Punctuation:", cleaner.remove_punctuation(text))
    print("Remove Stop Words:", cleaner.remove_stop_words(text))
    print("Lowercase:", cleaner.lowercase(text))
    print("Remove Numbers:", cleaner.remove_numbers(text))
    print("Normalize Whitespace:", cleaner.normalize_whitespace(text))
    print("Remove Special Characters:", cleaner.remove_special_characters(text))
    print("Remove HTML Tags:", cleaner.remove_html_tags(text))
    print("Remove URLs/Emails:", cleaner.remove_urls_emails(text))
    print("Clean All:", cleaner.clean_all(text))