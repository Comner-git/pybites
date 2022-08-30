import math

def round_up_or_down(transactions, up=True):
    """Round the list of transactions passed in.
       If up=True (default) round up, else round down.
       Return a new list of rounded values
    """
    rounded = []
    for x in transactions:
        if up:
            rounded.append(math.ceil(x))
        else:
            rounded.append(math.floor(x))
    return rounded
    pass
