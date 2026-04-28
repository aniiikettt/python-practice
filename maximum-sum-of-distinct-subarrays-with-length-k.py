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

           
            if right - left + 1 > k:
                left_num = nums[left]
                freq[left_num] -= 1
                if freq[left_num] == 0:
                    del freq[left_num]    
                current_sum -= left_num
                left += 1

            
            if right - left + 1 == k:
                if len(freq) == k:        
                    max_sum = max(max_sum, current_sum)

        return max_sum