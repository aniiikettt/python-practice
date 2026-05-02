class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        
        basket = {}      # fruit_type → count in window
        left = 0
        max_fruits = 0