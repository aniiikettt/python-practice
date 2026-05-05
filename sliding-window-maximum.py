from collections import deque

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        
        dq = deque()    # Stores INDICES, front = index of max
        result = []

        for right in range(len(nums)):

            # Step 1: Remove EXPIRED index from front
            # (index no longer in window [right-k+1 ... right])
            if dq and dq[0] < right - k + 1:
                dq.popleft()