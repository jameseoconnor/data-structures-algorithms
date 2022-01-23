import math

class Solution:
    def minEatingSpeed(self, piles, h) -> int:
        # initial speed
        speed = 1

        while True: 
            hours_spent = 0 

            for pile in piles: 
                hours_spent += math.ceil(pile / speed)

            if hours_spent <= h: 
                return speed
            
            else: 
                speed +=1


sol = Solution()
test_case = [3,6,7,11,12]
hours = 8 

test = sol.minEatingSpeed(test_case, hours)
print(test)