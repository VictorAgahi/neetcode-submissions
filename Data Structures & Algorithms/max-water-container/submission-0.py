class Solution:
    def maxArea(self, heights: List[int]) -> int:
        max_area = 0
        # max aera = min(height[x], height[y]) * (y - x) with y > x
        right = 0
        left = len(heights) - 1
        while right < left:
            current_area = min (heights[right], heights[left]) * (left - right)
            if current_area > max_area:
                max_area = current_area
            else:
                if heights[left] > heights[right]:
                    right += 1
                else:
                    left -= 1
        return max_area