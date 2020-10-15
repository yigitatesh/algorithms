
def fibonacci(n_numbers=10, end_number=None):
	"""Fibonacci series
	iterative sum of last two implementation

	Parameters
	----------
	n_numbers: number of numbers in fibonacci series
	end_number: upper bound of series"""
	fib_series = [1]
	first = 0
	second = 1
	for _ in range(n_numbers - 1):
		# second is sum of two
		# first is second
		second = first + second
		first = second - first

		if not end_number is None:
			if second > end_number:
				return fib_series

		fib_series.append(second)

	return fib_series

def fibonacci_golden(n_numbers=10, end_number=None):
    """Fibonacci series
    Golden Ratio implementation
    golden ratio = 1.618...
    next element = last element * golden ratio
    
    !!!
    There is an upper bound when elements reach infinity
        -> 1476 is a possible limit
    Raises an error when this limit exceeded

    Parameters
    ----------
    n_numbers: number of numbers in fibonacci series
    end_number: upper bound of series"""
    if n_numbers == 1:
        return [1]
    golden_ratio = 1.618
    inf = float("inf")
    fib_series = [1, 1]
    for _ in range(n_numbers - 2):
        next_raw = fib_series[-1] * golden_ratio
        if next_raw == inf:
            raise BaseException("Number limit exceeded")
        next = round(next_raw)
        if not end_number is None:
            if next > end_number:
                return fib_series

        fib_series.append(next)

    return fib_series
