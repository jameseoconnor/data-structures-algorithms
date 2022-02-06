# Brute Force Approach - This one is N^2 
# class Solution:
#     def maxProfit(self, prices) -> int:
#         largest_profit = 0
#         for i in range(len(prices)): 
#             for j in range(i, len(prices)): 
#                 if prices[j] - prices[i] > largest_profit:
#                     largest_profit = prices[j] - prices[i]
        
#         return largest_profit

class Solution:
    def maxProfit(self, prices) -> int:
        largest_difference_seen = 0 

        # The lowest price is always the first one 
        lowest_price_so_far = prices[0]

        # Start loop at prices[1]
        for i in range(1, len(prices)): 

            # If we find a bigger difference using our current variables \ 
            # for largest and lowest, we store it as the new largest diff
            if prices[i] - lowest_price_so_far > largest_difference_seen: 
                largest_difference_seen = prices[i] - lowest_price_so_far
            
            # If we find a price that is lower than our current lowest \ 
            # then we store this and use this in the next iteration of the \ 
            # calculation above
            if prices[i] < lowest_price_so_far: 
                lowest_price_so_far = prices[i]
        
        return largest_difference_seen


sol = Solution()
test_case = [1,2]
test_case_pass_result = 5

test = sol.maxProfit(test_case)

if test == test_case_pass_result:
    print("Test passed")