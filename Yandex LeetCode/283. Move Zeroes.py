"""
Given an integer array nums, move all 0's to the end
of it while maintaining the relative order of the non-zero elements.

Note that you must do this in-place without making a copy of the array.
"""


class Solution:
    def moveZeroes(self, nums):
        """
        1. if the number is 0 then we only increment the pointer named "second".
        2. if the number is not 0 we swap the number of pointers.
        2. if the number is not 0 then we increment both pointers.
        """
        first = 0
        for second in range(len(nums)):
            if nums[second] != 0:
                nums[first], nums[second] = nums[second], nums[first]
                first += 1


print(Solution().moveZeroes(nums=[0, 1, 0, 3, 12]))