
def fibonacci(n_numbers=10, end_number=None):
	"""Fibonacci series

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