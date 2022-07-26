import string


def get_index_different_char(chars):
    alpha = string.ascii_letters + string.digits
    count = 0
    notalphaindex = 0
    alphaindex = 0
    for index, item in enumerate(chars):
        if str(item) not in alpha:
            notalphaindex = index
            count += 1
        else:
            alphaindex = index
            pass
    if count > 1:
        return alphaindex
    return notalphaindex
    pass
