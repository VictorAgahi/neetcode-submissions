class Solution:
    def maxArea(self, heights: List[int]) -> int:
        max_area = 0
        right = len(heights) - 1
        left = 0
        """
            area = min(height[right], height[left]) * (right - left)
        """
        while left < right:
            area = min(heights[right], heights[left]) * (right - left)
            if area > max_area:
                max_area = area
            if heights[right] > heights[left]:
                left += 1
            else:
                right -= 1
        return max_area