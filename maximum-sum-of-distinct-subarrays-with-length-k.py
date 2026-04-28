class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        
        freq = {}          # Tracks count of each element in window
        current_sum = 0    # Sum of current window
        max_sum = 0        # Best valid sum found
        left = 0           # Left boundary of windowclass Solution:

        for right in range(len(nums)):
            
            # Step 1: Add new right element to window
            num = nums[right]
            freq[num] = freq.get(num, 0) + 1
            current_sum += num

            # Step 2: If window size exceeds k, shrink from left
            if right - left + 1 > k:
                left_num = nums[left]
                freq[left_num] -= 1
                if freq[left_num] == 0:
                    del freq[left_num]    # Clean up zero counts
                current_sum -= left_num
                left += 1

            # Step 3: Window is exactly size k → check if valid
            if right - left + 1 == k:
                if len(freq) == k:        # All elements distinct!
                    max_sum = max(max_sum, current_sum)

        return max_sum