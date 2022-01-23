# class Solution:
#     def twoSum(self, nums, target):
        
#         for i in range(len(nums)):
#             for j in range(i + 1, len(nums)):
#                 if nums[j] == target - nums[i]:
#                     return [i, j]


# Memoization in action

class Solution:
    def twoSum(self, nums, target):
        memo = set()

        for i in range(len(nums)):
            complement = target - nums[i]

            if complement in memo:
                return [i, memo[complement]]
            memo[nums[i]] = i



sol = Solution()
test_case = [4,1,5,6,7,3]
target = 8


test = sol.twoSum(test_case, target)
print(test)