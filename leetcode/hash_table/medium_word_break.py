# Given a string s and a dictionary of strings wordDict,
# return true if s can be segmented into
# a space-separated sequence of one or more dictionary words.

# Note that the same word in the dictionary may be reused multiple times
# in the segmentation.
from typing import Dict, List, Set


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:

        memory = {}

        def can_construct(target: str, words: List[str], memory: dict) -> bool:
            if target == "":
                return True
            if target in memory:
                return memory[target]
            for word in words:
                if target.startswith(word):
                    print(f"starting {word}")
                    if can_construct(target[len(word) :], words, memory):
                        memory[target] = True
                        print(memory)
                        return True
            memory[target] = False
            return False

        return can_construct(s, wordDict, memory)


if __name__ == "__main__":
    solution = Solution()
    s = "leetcodeeee"
    wordDict = ["leet", "eee", "codee", "ee"]

    print(solution.wordBreak(s=s, wordDict=wordDict))
