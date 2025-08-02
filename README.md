# Text Cleaning Library

## Overview
The **Text Cleaning Library** provides a Python `Cleaner` class for preprocessing raw text data, making it suitable for natural language processing (NLP), data analysis, or machine learning tasks. It removes noise (e.g., punctuation, stop words, special characters) and standardizes text format to improve consistency and model performance. The library is lightweight, modular, and uses only standard Python libraries (`re`, `string`).

## Features
- **Modular Methods**: Separate functions for each cleaning operation (e.g., punctuation removal, stop word removal).
- **Lightweight**: No external dependencies, using only Python’s standard libraries.
- **Comprehensive Testing**: Includes a test suite (`test_cleaner.py`) that verifies all methods, with all tests passing.
- **Flexible**: Supports individual cleaning operations or a combined `clean_all` method for full preprocessing.
- **Open-Source**: Licensed under the MIT License for easy reuse and modification.

## What is Text Cleaning?
Text cleaning is the process of preprocessing raw text to remove irrelevant or noisy elements (e.g., punctuation, stop words, URLs) and standardize its format (e.g., lowercase, normalized whitespace). It is a critical step in NLP, text mining, and data analysis to prepare text for tasks like tokenization, sentiment analysis, or machine learning.

### Why is Text Cleaning Used?
- **Remove Noise**: Eliminates irrelevant elements (e.g., punctuation, numbers) that don’t contribute to meaning.
- **Standardize Text**: Ensures consistent format (e.g., lowercase, single spaces) for uniform processing.
- **Reduce Complexity**: Removes stop words or redundant terms to focus on meaningful content.
- **Improve Model Accuracy**: Cleaned text enhances feature extraction for NLP tasks.
- **Enable Downstream Processing**: Prepares text for tokenization, chunking, or other analysis.

### Supported Cleaning Methods
The `Cleaner` class provides the following methods:
1. **Punctuation Removal** (`remove_punctuation`): Removes punctuation marks (e.g., "Hello!" → "Hello").
2. **Stop Word Removal** (`remove_stop_words`): Removes common words like "the", "is" (e.g., "The cat is on" → "cat").
3. **Lowercasing** (`lowercase`): Converts text to lowercase (e.g., "Hello WORLD" → "hello world").
4. **Number Removal** (`remove_numbers`): Removes digits (e.g., "I have 2 cats" → "I have cats").
5. **Whitespace Normalization** (`normalize_whitespace`): Removes extra spaces and trims (e.g., "  Hello   world  " → "Hello world").
6. **Special Character Removal** (`remove_special_characters`): Removes non-alphanumeric characters except spaces (e.g., "Hello @world!" → "Hello world").
7. **HTML Tag Removal** (`remove_html_tags`): Strips HTML/XML tags (e.g., "<p>Hello</p>" → "Hello").
8. **URL/Email Removal** (`remove_urls_emails`): Removes URLs and email addresses (e.g., "Visit http://example.com" → "Visit").
9. **Full Cleaning** (`clean_all`): Applies all methods in sequence for comprehensive preprocessing.

## Installation
1. **Clone the Repository**:
   ```bash
   git clone https://github.com/<your-username>/cleaning.git
   cd cleaning
   ```
2. **(Optional) Create a Virtual Environment**:
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```
3. **Use the Library**:
   Copy `cleaner.py` to your project or add the repository folder to your Python path.

4. **(Optional) Install via PyPI** (if published):
   ```bash
   pip install cleaning
   ```

## Usage
The `Cleaner` class provides individual methods for specific cleaning tasks or a `clean_all` method for full preprocessing.

### Example
```python
from cleaner import Cleaner

cleaner = Cleaner()
text = "  The <b>Cat</b> is 123 @on the http://example.com mat!!!  "

# Individual cleaning methods
print(cleaner.remove_punctuation(text))  # Output: "The Cat is 123 on the http://example.com mat"
print(cleaner.remove_stop_words(text))   # Output: "Cat 123 @on mat!!!"
print(cleaner.lowercase(text))           # Output: "the <b>cat</b> is 123 @on the http://example.com mat!!!"
print(cleaner.remove_numbers(text))      # Output: "The <b>Cat</b> is @on the http://example.com mat!!!"
print(cleaner.normalize_whitespace(text)) # Output: "The <b>Cat</b> is 123 @on the http://example.com mat!!!"
print(cleaner.remove_special_characters(text)) # Output: "The Cat is 123 on the httpexamplecom mat"
print(cleaner.remove_html_tags(text))    # Output: "The Cat is 123 @on the http://example.com mat!!!"
print(cleaner.remove_urls_emails(text))  # Output: "The Cat is or"

# Full cleaning
print(cleaner.clean_all(text))           # Output: "cat mat"
```

### Running the Example Script
```bash
python3 cleaner.py
```

### Testing
The `test_cleaner.py` file includes a comprehensive test suite for all cleaning methods, covering valid inputs and edge cases. Run it with:
```bash
python3 -m unittest test_cleaner.py -v
```

**Expected Output**:
```
test_clean_all (test_cleaner.TestCleaner.test_clean_all) ... ok
test_lowercase (test_cleaner.TestCleaner.test_lowercase) ... ok
test_normalize_whitespace (test_cleaner.TestCleaner.test_normalize_whitespace) ... ok
test_remove_html_tags (test_cleaner.TestCleaner.test_remove_html_tags) ... ok
test_remove_numbers (test_cleaner.TestCleaner.test_remove_numbers) ... ok
test_remove_punctuation (test_cleaner.TestCleaner.test_remove_punctuation) ... ok
test_remove_special_characters (test_cleaner.TestCleaner.test_remove_special_characters) ... ok
test_remove_stop_words (test_cleaner.TestCleaner.test_remove_stop_words) ... ok
test_remove_urls_emails (test_cleaner.TestCleaner.test_remove_urls_emails) ... ok
----------------------------------------------------------------------
Ran 9 tests in 0.001s
OK
```

## Project Structure
```
cleaning/
├── cleaner.py           # Core cleaning library
├── test_cleaner.py     # Test suite
├── README.md           # Project documentation
├── .gitignore          # Git ignore file
├── LICENSE             # MIT License
├── setup.py            # (Optional) PyPI packaging
```

## Requirements
- Python 3.6 or higher
- No external dependencies (uses `re` and `string` from the standard library)

## Using in Other Projects
1. **Local Copy**:
   - Copy `cleaner.py` to your project folder.
   - Import:
     ```python
     from cleaner import Cleaner
     cleaner = Cleaner()
     text = "Hello @world! http://example.com"
     print(cleaner.clean_all(text))  # Output: "hello world"
     ```

2. **Git Submodule**:
   - Add as a submodule:
     ```bash
     cd /path/to/your/project
     git submodule add https://github.com/<your-username>/cleaning.git
     ```
   - Import as above, ensuring the `cleaning` folder is in your Python path.

3. **PyPI Installation** (if published):
   - Install:
     ```bash
     pip install cleaning
     ```
   - Import:
     ```python
     from cleaner import Cleaner
     ```

## Example Integration with Chunking
If you have the `chunking` library (from https://github.com/<your-username>/chunking), you can combine cleaning and chunking:
```python
from cleaner import Cleaner
from chunking import Chunker  # Assuming chunking is in your Python path
cleaner = Cleaner()
chunker = Chunker()
text = "The quick fox jumps"
cleaned = cleaner.clean_all(text)  # Output: "quick fox jumps"
# Assume POS tagging is done elsewhere
tagged = [('quick', 'JJ'), ('fox', 'NN'), ('jumps', 'VB')]
chunks = chunker.semantic_chunking(tagged)
print(chunks)  # Output: [('quick fox', [('quick', 'JJ'), ('fox', 'NN')])]
```

## Contributing
Contributions are welcome! To contribute:
1. Fork the repository.
2. Create a feature branch (`git checkout -b feature/new-feature`).
3. Commit changes (`git commit -m "Add new feature"`).
4. Push to the branch (`git push origin feature/new-feature`).
5. Open a pull request.

Please include tests for new features in `test_cleaner.py` and ensure all tests pass.

## Troubleshooting
- **Tests Fail**: Verify `cleaner.py` and `test_cleaner.py` match the provided code. Debug with:
  ```python
  print("Result:", result)
  print("Expected:", expected)
  ```
- **Import Errors**: Ensure `cleaner.py` is in your project folder or Python path. Reinstall virtual environment if needed:
  ```bash
  rm -rf venv
  python3 -m venv venv
  source venv/bin/activate
  ```
- **Regex Issues**: Test regex patterns with:
  ```python
  import re
  text = "Visit http://example.com or test@domain.com"
  print(re.sub(r'https?://\S+|www\.\S+', '', text))
  ```
- **Performance**: For large texts, profile with:
  ```python
  import time
  cleaner = Cleaner()
  start = time.time()
  cleaner.clean_all("large text " * 1000)
  print(f"Time: {time.time() - start}")
  ```

## License
This project is licensed under the MIT License. See the `LICENSE` file for details.