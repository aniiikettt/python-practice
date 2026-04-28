class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        
        freq = {}          # Tracks count of each element in window
        current_sum = 0    # Sum of current window
        max_sum = 0        # Best valid sum found
        left = 0           # Left boundary of windowclass Solution: