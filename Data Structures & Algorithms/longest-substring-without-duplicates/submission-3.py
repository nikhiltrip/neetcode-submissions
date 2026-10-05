class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0
        seen = set()
        maxl = 0

        right = 0
        while right < len(s):
            while s[right] in seen:
                seen.remove(s[left])
                left += 1
            
            
            seen.add(s[right])
            window = right - left + 1
            maxl = max(maxl, window)
            right += 1
        
        return maxl

            
            
            
            