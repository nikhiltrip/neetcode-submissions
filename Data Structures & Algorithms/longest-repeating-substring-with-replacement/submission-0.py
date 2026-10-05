class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        left = 0
        maxl = 0

        right = 0
        counts = {}
        while right < len(s):
            counts[s[right]] = counts.get(s[right], 0) + 1
            a = (right - left + 1) - max(counts.values())
            while a > k:
                counts[s[left]] -= 1
                left += 1
                a = (right - left + 1) - max(counts.values())

            maxl = max(maxl, right - left + 1)

            right += 1
        
        return maxl
