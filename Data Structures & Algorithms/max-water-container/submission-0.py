class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left, right = 0, len(heights) - 1
        maxa = 0

        while left < right:
            width = right - left
            area = min(heights[right], heights[left]) * width
            if area > maxa:
                maxa = area

            elif heights[left] < heights[right]:
                left += 1
            else:
                right -= 1
        
        return maxa