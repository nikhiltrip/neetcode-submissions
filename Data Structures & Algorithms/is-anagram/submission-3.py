from collections import defaultdict
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        counts_s=defaultdict(int)
        counts_t=defaultdict(int)

        for char in s:
            counts_s[char] += 1

        for char in t:
            counts_t[char] += 1

        return counts_s == counts_t