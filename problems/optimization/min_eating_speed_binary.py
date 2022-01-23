import math

class Solution:
    def minEatingSpeed(self, piles, h):
        # initial speed
        left = 1
        right = max(piles)

        # [1,.,6,.,12] - binary search
        # [3,6,7,11,12]


        while left < right:
            middle = (left + right) // 2
            hours_spent = 0

            for pile in piles:
                hours_spent += math.ceil(pile / middle)

            if hours_spent <= h:
                right = middle
            else: 
                left = middle + 1

        return right


sol = Solution()
test_case = [3,6,7,11,12]
hours = 8 

test = sol.minEatingSpeed(test_case, hours)
print(test)