class Solution:
    from typing import List
    def maxArea(self, height: List[int]) -> int:

        left = 0
        right = len(height) - 1
        max_water = 0

        while left < right:

            width = right - left
            h = min(height[left], height[right])
            current_water = width * h

            max_water = max(max_water, current_water)

            if height[left] < height[right]:
                left += 1
            else:
                right -= 1

        return max_water