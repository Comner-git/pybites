from enum import Enum
from collections import Counter


class Equality(Enum):
    SAME_REFERENCE = 4
    SAME_ORDERED = 3
    SAME_UNORDERED = 2
    SAME_UNORDERED_DEDUPED = 1
    NO_EQUALITY = 0


def check_equality(list1, list2):
    """Check if list1 and list2 are equal returning the kind of equality.
       Use the values in the Equality Enum:
       - return SAME_REFERENCE if both lists reference the same object
       - return SAME_ORDERED if they have the same content and order
       - return SAME_UNORDERED if they have the same content unordered
       - return SAME_UNORDERED_DEDUPED if they have the same unordered content
         and reduced to unique items
       - return NO_EQUALITY if none of the previous cases match"""
    if list1 is list2:
        return Equality.SAME_REFERENCE
    if list1 == list2:
        return Equality.SAME_ORDERED
    if Counter(list1) == Counter(list2):
        return Equality.SAME_UNORDERED
    if Counter(list(dict.fromkeys(list1))) == Counter(list(dict.fromkeys(list2))):
        return Equality.SAME_UNORDERED_DEDUPED
    else:
        return Equality.NO_EQUALITY
    pass
