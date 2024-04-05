"""
REVERSE AN INTEGER - Problem Statement
Given an integer, reverse it.
320 --> 23
-321 --> -123
"""
"""
Thought Process:
"""

def reversed_int(n: int) -> int:
	"""
	Params: n, an integer in the range -2^31 <= n <= 2^31
	"""
	if n <= -(2 ** 31) or n >= (2 ** 31):
		return 0
	if n < 0:
		n = n * -1
		return -1 * int(str(n)[::-1])
	else:
		return int(str(n)[::-1])

if __name__ == '__main__':
	print(reversed_int(320))
	print(reversed_int(-321))
	print(reversed_int(-32))
	print(reversed_int(32))
	print(reversed_int(123456789101112))