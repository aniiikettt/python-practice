class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        
        nums.sort()           
        result = []

        for i in range(len(nums) - 2):    
            
           
            if nums[i] > 0:
                break

           
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            