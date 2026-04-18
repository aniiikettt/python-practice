print("FILE IS RUNNING")
from typing import List

class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        pos = 0

        for i in range(len(nums)):
            if nums[i] != 0:
                nums[pos] = nums[i]
                pos += 1

        while pos < len(nums):
            nums[pos] = 0
            pos += 1

        if __name__ == "__main__":
            nums = [0,1,0,3,12]
            Solution().moveZeroes(nums)
            print(nums)