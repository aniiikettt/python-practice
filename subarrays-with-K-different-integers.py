class Solution:
    def subarraysWithKDistinct(self, nums: List[int], k: int) -> int:
        
        def at_most(k):
            """Count subarrays with AT MOST k distinct integers"""
            freq = {}
            left = 0
            count = 0

            for right in range(len(nums)):

                # Add right element
                num = nums[right]
                freq[num] = freq.get(num, 0) + 1

                # Shrink while more than k distinct
                while len(freq) > k:
                    left_num = nums[left]
                    freq[left_num] -= 1
                    if freq[left_num] == 0:
                        del freq[left_num]
                    left += 1