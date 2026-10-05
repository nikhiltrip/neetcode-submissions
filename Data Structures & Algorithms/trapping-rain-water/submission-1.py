class Solution:
    def trap(self, height: List[int]) -> int:
        if not height:
            return 0
        
        left, right = 0, len(height) - 1
        left_max, right_max = height[left], height[right]

        total = 0
        while left < right:
            if height[left] > left_max:
                left_max = height[left]
            if height[right] > right_max:
                right_max = height[right]
            if left_max <= right_max:
                total += left_max - height[left]
                left += 1
            else:
                total += right_max - height[right]
                right -= 1
            
        return total