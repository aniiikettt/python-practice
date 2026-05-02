class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        
        basket = {}      # fruit_type → count in window
        left = 0
        max_fruits = 0

        for right in range(len(fruits)):

            # Step 1: Add right fruit to basket
            fruit = fruits[right]
            basket[fruit] = basket.get(fruit, 0) + 1