
def lcm(first, second):
    """Calculate least common multiplier of two integers"""
    if first < 0 or second < 0:
        return None

    # make first bigger of two
    if first < second:
        first, second = second, first
    # increase big number until two numbers are same
    raw_first = first
    while first % second:
        first += raw_first

    return first