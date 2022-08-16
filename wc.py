import ntpath

def wc(file_):
    """Takes an absolute file path/name, calculates the number of
       lines/words/chars, and returns a string of these numbers + file, e.g.:
       3 12 60 /tmp/somefile
       (both tabs and spaces are allowed as separator)"""
    file = open(file_, "r")
    content = file.read()
    lines = content.splitlines(True)
    words = content.split()
    chars = list(content)
    result = [len(lines), len(words), len(chars), ntpath.basename(file_)]
    return '\t'.join(map(str, result))
    pass

if __name__ == '__main__':
    # make it work from cli like original unix wc
    import sys
    print(wc(sys.argv[1]))
