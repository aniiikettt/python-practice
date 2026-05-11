class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        n = len(nums)
        left  = [1] * n    # left[i]  = product of nums[0..i-1]
        right = [1] * n    # right[i] = product of nums[i+1..n-1] 