# Given two strings s and t,
# return true if s is a subsequence of t,
# or false otherwise.

# A subsequence of a string is a new string
# that is formed from the original string
# by deleting some (can be none) of the characters
# without disturbing the relative positions
# of the remaining characters.

# (i.e., "ace" is a subsequence of "abcde" while "aec" is not).

# Input: s = "abc", t = "ahbgdc"
# Output: true

# this is also a dp problem
class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:

        # just an edge case..
        if s == "":
            return True

        score = 0

        for char in t:
            if char == s[score]:
                score += 1
                if score == len(s):
                    return True
        return False


if __name__ == "__main__":
    s = Solution()
    print(s.isSubsequence(s="be", t="abcadsfae"))
