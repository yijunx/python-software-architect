# Given an integer array nums,
# return all the triplets
#  [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k,
# and nums[i] + nums[j] + nums[k] == 0.

# Notice that the solution set must not contain duplicate triplets.
from typing import List


class Solution:
    def threeSum(self, nums: List[int], target: int = 0) -> List[List[int]]:

        solutions = []
        nums.sort()
        for i, first_num in enumerate(nums):

            if i > 0 and first_num == nums[i - 1]:
                continue

            l, r = i + 1, len(nums) - 1

            while l < r:
                curr_sum = nums[l] + nums[r] + first_num
                if curr_sum > target:
                    r -= 1
                elif curr_sum < target:
                    l += 1
                else:
                    solutions.append([nums[x] for x in [i, l, r]])
                    l += 1
                    while nums[l] == nums[l - 1] and l < r:
                        l += 1
        return solutions


if __name__ == "__main__":
    s = Solution()
    print(s.threeSum([-1, 0, 1, 2, -1, -4], 3))
