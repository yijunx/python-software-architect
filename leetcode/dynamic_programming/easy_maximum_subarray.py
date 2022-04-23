# Given an integer array nums,
# find the contiguous subarray
# (containing at least one number)
# which has the largest sum and return its sum.

# A subarray is a contiguous part of an array.

# Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
# Output: 6
# Explanation: [4,-1,2,1] has the largest sum = 6.
from typing import List


class Solution:  # this is a dp problem
    def maxSubArray(self, nums: List[int]) -> int:
        max_sum_ends_at_i = [nums[0]] * len(nums)
        # max_checked_sofar = [nums[0]] * len(nums)

        for i, num in enumerate(nums[1:]):
            max_sum_ends_at_i[i + 1] = max(num, max_sum_ends_at_i[i] + num)
            # this max is the key to the problem
            # if number is bigger than what all number before it can do with itself,
            # then we know all the stuff before this number can be discarded
            # so we can know where is the max

        print(max_sum_ends_at_i)
        # print(max_checked_sofar)
        return max(max_sum_ends_at_i)


if __name__ == "__main__":
    s = Solution()
    print(s.maxSubArray([-2, 1, -3, 4, -1, 2, 1, -5, 4]))
