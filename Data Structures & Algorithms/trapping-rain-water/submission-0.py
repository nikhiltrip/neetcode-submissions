class Solution:
    def trap(self, height: List[int]) -> int:
        if not height:
            return 0
        
        left_max = [0] * (len(height))
        right_max = [0] * (len(height))

        tallest = 0
        for i in range(len(height)):
            tallest = max(tallest, height[i])
            left_max[i] = tallest
        
        tallest = 0
        for i in range(len(height) - 1, -1, -1):
            tallest = max(tallest, height[i])
            right_max[i] = tallest

        total = 0
        for i in range (len(height)):
            total += max(0, min(left_max[i], right_max[i]) - height[i])
        
        return total