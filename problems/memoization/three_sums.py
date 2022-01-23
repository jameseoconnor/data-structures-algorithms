class Solution:
    def threeSum(self, nums):
        # i = 0 
        # j = i + 1
        # k = j + 1
#         target = 0  -> i + j + k = 0 
#         Create a memo as we pass through so we can save the numbers we passed
        res, dups = set(), set()
        seen = {}
        for i, val1 in enumerate(nums):
            if val1 not in dups:
                dups.add(val1)
                for j, val2 in enumerate(nums[i+1:]):
                    complement = -val1 - val2
                    if complement in seen and seen[complement] == i:
                        res.add(tuple(sorted((val1, val2, complement))))
                    seen[val2] = i
        return res

sol = Solution()
test_case = [-1,0,1,2,-1,-4]
# target = 8


test = sol.threeSum(test_case)
print(test)