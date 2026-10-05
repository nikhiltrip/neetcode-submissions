from collections import defaultdict
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1_counts = defaultdict(int)
        for char in s1:
            s1_counts[char] += 1
        
        left = 0

        if len(s1) > len(s2):
            return False

        s2_counts = defaultdict(int)
        
        right = len(s1) - 1

        for char in s2[left : right + 1]:
            s2_counts[char] += 1
        
        if s1_counts == s2_counts:
            return True
        
        while right < len(s2):
            if s1_counts != s2_counts:
                s2_counts[s2[left]] -= 1
                if s2_counts[s2[left]] == 0:
                    del s2_counts[s2[left]]
                left += 1
                if right == len(s2) - 1:
                    return False
                right += 1
                s2_counts[s2[right]] += 1

            if s1_counts == s2_counts:
                return True
            
        return False