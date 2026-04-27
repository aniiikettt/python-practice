class Solution:
    from typing import List
    def trap(self, height: List[int]) -> int:

        n = len(height)
        if n == 0:
            return 0
        
        left_max = [0] * n
        left_max[0] = height[0]
        for i in range(1 , n):
            left_max[i] = max(left_max[i-1], height[i])
