class Solution:  # the use of binary search
    def isPerfectSquare(self, num: int) -> bool:

        if num == 1 or num == 4:
            return True

        lb = 1
        rb = num // 2

        while rb > lb + 1:
            mid_effect = ((rb + lb) // 2) ** 2
            if mid_effect == num:
                return True
            elif mid_effect > num:
                rb = (rb + lb) // 2
            else:
                lb = (rb + lb) // 2
        return False


if __name__ == "__main__":
    s = Solution()
    print(s.isPerfectSquare(4))
    print(s.isPerfectSquare(5))
    print(s.isPerfectSquare(6))
    print(s.isPerfectSquare(9))
