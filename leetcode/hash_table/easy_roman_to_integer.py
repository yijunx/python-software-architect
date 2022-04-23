class Solution:  # some use of hashtable
    def romanToInt(self, s: str) -> int:

        symbol_mappings = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000,
        }

        # rules
        # I can be placed before V (5) and X (10) to make 4 and 9.
        # X can be placed before L (50) and C (100) to make 40 and 90.
        # C can be placed before D (500) and M (1000) to make 400 and 900.

        minus_mappings = {"I": {"V", "X"}, "X": {"L", "C"}, "C": {"D", "M"}}
        r = 0
        for i, char in enumerate(s):
            if (
                i < len(s) - 1
                and char in minus_mappings
                and s[i + 1] in minus_mappings[char]
            ):
                r -= symbol_mappings[char]
            else:
                r += symbol_mappings[char]
        return r


if __name__ == "__main__":
    s = Solution()
    print(s.romanToInt("MDCI"))
    print(s.romanToInt("MDIV"))
