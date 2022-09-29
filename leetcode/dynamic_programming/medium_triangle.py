# Given a triangle array,
# return the minimum path sum from top to bottom.

# For each step,
# you may move to an adjacent number of the row below.
# More formally,
# if you are on index i on the current row,
# you may move to either index i or index i + 1
# on the next row.

# Input: triangle = [[2],[3,4],[6,5,7],[4,1,8,3]]
# Output: 11
# Explanation: The triangle looks like:
#    2
#   3 4
#  6 5 7
# 4 1 8 3
# The minimum path sum from top to bottom is
# 2 + 3 + 5 + 1 = 11 (underlined above).

from typing import List


class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        # min_sum_to_each_pos = triangle.copy()
        # say len(triangle) jas 4 layers, 0,1,2,3
        layer = len(triangle) - 2  # start with layer 2
        while layer >= 0:
            for i, element in enumerate(triangle[layer]):
                triangle[layer][i] = min(
                    element + triangle[layer + 1][i],
                    element + triangle[layer + 1][i + 1],
                )

            layer -= 1
        return triangle[0][0]


if __name__ == "__main__":
    s = Solution()
    print(s.minimumTotal([[2], [3, 4], [6, 5, 7], [4, 3, 8, 1]]))
