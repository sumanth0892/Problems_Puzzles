"""
Given an unsorted integer array nums. Return the smallest positive integer that is not present in nums.

You must implement an algorithm that runs in O(n) time and uses O(1) auxiliary space.

 

Example 1:

Input: nums = [1,2,0]
Output: 3
Explanation: The numbers in the range [1,2] are all in the array.
Example 2:

Input: nums = [3,4,-1,1]
Output: 2
Explanation: 1 is in the array but 2 is missing.
Example 3:

Input: nums = [7,8,9,11,12]
Output: 1
Explanation: The smallest positive integer 1 is missing.
 

Constraints:

1 <= nums.length <= 105
-231 <= nums[i] <= 231 - 1
"""
class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        nums = sorted(nums)
        nums = [n for n in nums if n > 0]
        nums = sorted(list(set(nums)))
        if len(nums) == 0:
            return 1
        if len(nums) == 1:
            if nums[0] <= 0:
                return 1
            if nums[0] == 1:
                return 2
            if nums[0] > 1:
                return 1
        if min(nums) == 1 and nums[1] != 2:
            return 2
        if min(nums) > 1:
            return 1
        if len(nums) == max(nums):
            return max(nums) + 1
        for i in range(max(nums)):
            if nums[i] != i + 1:
                return (nums[i - 1] + 1)
