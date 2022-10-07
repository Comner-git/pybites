def convert(value: float, fmt: str) -> float:
    """Converts the value to the designated format.

    :param value: The value to be converted must be numeric or raise a TypeError
    :param fmt: String indicating format to convert to
    :return: Float rounded to 4 decimal places after conversion
    """
    if type(value) not in {int, float}:
        raise TypeError()
    elif fmt.lower() not in {"in", "cm"}:
        raise ValueError()
    elif fmt.lower() == "in":
        return round(value/2.54, 4)
    elif fmt.lower() == "cm":
        return round(value*2.54, 4)
    pass
