import re
import string

VOWELS = 'aeiou'
PYTHON = 'python'


def contains_only_vowels(input_str):
    """Receives input string and checks if all chars are
       VOWELS. Match is case insensitive."""
    return bool(re.search(f'(?i)^[{VOWELS}]+$', input_str))
    pass


def contains_any_py_chars(input_str):
    """Receives input string and checks if any of the PYTHON
       chars are in it. Match is case insensitive."""
    return bool(re.search(f'(?i)[{PYTHON}]', input_str))
    pass


def contains_digits(input_str):
    """Receives input string and checks if it contains
       one or more digits."""
    return bool(re.search(f'\d', input_str))
    pass
