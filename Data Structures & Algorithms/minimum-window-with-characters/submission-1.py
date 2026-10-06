from collections import defaultdict
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        t_counts = defaultdict(int)
        for char in t:
            t_counts[char] += 1
        left = 0

        if len(t) > len(s):
            return ""

        s_counts = defaultdict(int)
        
        right = len(t) - 1

        for char in s[left : right + 1]:
            s_counts[char] += 1
        
        minl = float("inf")

        while right < len(s):
            valid = True
            for char, required in t_counts.items():
                if s_counts[char] < required:
                    valid = False
                    break
            if not valid and right < len(s) - 1:
                right += 1
                s_counts[s[right]] += 1
                continue
            if not valid and right == len(s) - 1:
                break
            while valid:
                curr = right - left + 1
                if curr < minl:
                    minl = curr
                    best_left = left
                l = left
                s_counts[s[l]] -= 1
                left += 1
                if s[l] in t_counts:
                    if s_counts[s[l]] < t_counts[s[l]]:
                        valid = False
                    
                    
        if minl == float("inf"):
            return ""
        
        return s[best_left : best_left + minl]

            