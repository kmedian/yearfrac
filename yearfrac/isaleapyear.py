
def isaleapyear(y: int) -> bool:
    if not isinstance(y, int):
        raise Exception("y is not an integer data type.")
    if y < 0:
        raise Exception("y is negative")

    return not(y % 4) and (bool(y % 100) or not(y % 400))
