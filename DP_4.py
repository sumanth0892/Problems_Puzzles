"""
MAXIMUM SUBARRAY - Problem Statement
Given an array of integers, find the sub-array with the largest sum and return the sum.
Example 1:
Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
Output: 6
Example 2:
Input: nums = [5,4,-1,7,8]
Output: 23
Example 3:
Input: nums = [1]
Output: 1
1 <= len(nums) <= 10 ^ 5

THOUGHT PROCESS:
The assumption is that we're considering the CONTIGUOUS SUB-ARRAYS only
Edge Case:
	If the length of the array is 1, return the element.
This is similar to the problem where we need to obtain the longest substring which is also a palindrome. 
1. We need to iterate over the items in the array and store the sum of the elements.
2. For each element, start with it and go until the end.
3. There has to be an efficient way to do this rather than employing a brute-force approach.
Consider a simple example:
nums = [5, 4, -1]
The subarrays are [5, 4], [4, -1] and [5, 4, -1]
The first element is 5 and using this, we iterate until the end as follows:
	[5, 4] and [5, 4, -1]
for EACH element:
	for i in range(len(array))
	sum[element] = element + elements appearing after the array, one by one
Let us store this as a 2D array with the rows and columns representing the elements of the input numbers array
This table appends elements if the sum is greater than the previous stored value
This algorithm runs in O(n ** 2) time and I believe can be further optimized.
"""
def get_max_sum(nums: list[int]) -> int:
	"""
	Get the sum of the subarray with the maximum sum.
	"""
	# Edge case
	if len(nums) == 1:
		return nums[0]
	n = len(nums); max_sum = 0
	A = [[0] * n for i in range(n)] 
	# Consider a bottom-up solution where we fill a table iteratively.
	for i in range(0, n):
		for j in range(0, n):
			if i == j:
				A[i][j] = nums[i]
			if i < j:
				A[i][j] = A[i][j - 1] + nums[j]
			elif i > j:
				A[i][j] = A[i - 1][j] + nums[i]
		if max_sum < max(A[i]):
			max_sum = max(A[i])
	for row in A:
		print(row)
	return max_sum

if __name__ =='__main__':
	print(get_max_sum([5, 4, -1, 7]))
	print("\n")
	print(get_max_sum([-2,1,-3,4,-1,2,1,-5,4]))
	print("\n")
	print(get_max_sum([5, 4, -1, 7, 8]))
