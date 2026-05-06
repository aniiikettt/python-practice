class Solution:
    def subarraysWithKDistinct(self, nums: List[int], k: int) -> int:
        
        def at_most(k):
            """Count subarrays with AT MOST k distinct integers"""
            freq = {}
            left = 0
            count = 0