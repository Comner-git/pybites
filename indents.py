import re
import pytest

def count_indents(text: str) -> int:
    """
    Count and return the number of leading white space characters (' ').
    """
    x = re.search("^ {1,}", text)
    if x:
        return len(x.group())
    else:
        return 0
    pass
