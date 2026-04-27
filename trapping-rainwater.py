class Solution:
    from typing import List
    def trap(self, height: List[int]) -> int:

        n = len(height)
        if n == 0:
            return 0
