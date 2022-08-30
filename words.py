import re

def sort_words_case_insensitively(words):
    """Sort the provided word list ignoring case, and numbers last
       (1995, 19ab = numbers / Happy, happy4you = strings, hence for
        numbers you only need to check the first char of the word)
    """
    words_s = sorted(words, key=str.casefold)
    nums = []
    for x in words_s:
        if re.search(r'^\d', x):
            nums.append(x)
    return words_s[len(nums)::]+words_s[:len(nums):]
    pass
