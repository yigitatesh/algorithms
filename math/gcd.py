
def gcd(first, second):
    """Calculate greatest common divisor of two integers"""
    if first < 0 or second < 0:
        return None

    while first != second:
        # make first bigger number
        if first < second:
            first, second = second, first

        # difference of two
        second = first - second
        # small number (variable second)
        first = first - second

    return first