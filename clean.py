import re
import string

def remove_punctuation(input_string):
    """Return a str with punctuation chars stripped out"""
    return re.sub(f'[{string.punctuation}]', '', input_string)
    pass
