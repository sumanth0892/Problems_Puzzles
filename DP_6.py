"""
LONGEST VALID PARANTHESIS - Problem Statement
Given a string containing just the characters '(' and ')' return the length of the longest valid paranthesis substring
s = "(()"
output = 2
s = ")()())"
ouptut = 4
Thought Process:
The first set of observations are:
	The output is in multiples of 2 since we have both opening and closing brackets.
	For every opening bracket, we need to have a closing bracket.
Attempt 1:
	Employ a stack structure which:
		adds an element when it encounters an opening bracket
		pops an element when it encounters a closing bracket
	At the end of the traversal, the difference between the length of the string and the number of elements in the stack gives the length of the longest valid paranthesis
	This algorithm runs in O(n) since we're traversing the string once.
	This occupies O(1) space since we're not adding any additional memory requirements.
Constraints:
0 <= s.length <= 30000
"""
def get_valid_length(s: str) -> int:
	"""
	params s: String of brackets
	output: An Integer with the longest valid string
	"""
	if len(s) == 0 or len(s) == 1:
		return "Invalid length"
	n = len(s); count_closed = 0
	stack = []
	for i in range(n):
		if s[i] == '(':
			stack.append(s[i])
		else:
			if len(stack) == 0:
				count_closed += 1
			else:
				stack.pop()
	return n - len(stack) - count_closed

if __name__ == '__main__':
	s = "(()"
	assert get_valid_length(s) == 2
	print(get_valid_length(s))
	s = ")()())"
	assert get_valid_length(s) == 4
	print(get_valid_length(s))
	s = "((()))"
	assert get_valid_length(s) == 6
	print(get_valid_length(s))