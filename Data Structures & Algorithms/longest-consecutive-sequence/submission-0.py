class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numbers = set(nums)
        maxlength = 0
        for number in numbers:
            current = number
            length = 1
            if number - 1 not in numbers:
                while current + 1 in numbers:
                    length += 1
                    current += 1
                if length > maxlength:
                    maxlength = length
        return maxlength