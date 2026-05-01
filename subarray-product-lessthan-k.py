class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        
        # Edge case: k <= 1 means no product can be < k
        if k <= 1:
            return 0

        left = 0
        product = 1      # Product of current window
        count = 0        # Total valid subarrays

        for right in range(len(nums)):

            # Step 1: Expand — multiply new right element
            product *= nums[right]

            # Step 2: Shrink — while product >= k
            while product >= k:
                product //= nums[left]   # Remove left element
                left += 1                # Shrink window

            # Step 3: Count new valid subarrays ending at 'right'
            count += right - left + 1

        return count