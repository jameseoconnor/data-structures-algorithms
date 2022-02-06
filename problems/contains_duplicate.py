class Solution:
    def containsDuplicate(self, nums) -> bool:
        hashmap = set()
        
        for i in range(len(nums)):
            if nums[i] in hashmap:
                return True
            hashmap.add(nums[i])
        
        return False

sol = Solution()
test_case = [1, 2, 3, 4, 5, 5, 6]
test_case_pass_result = True


test = sol.containsDuplicate(test_case)

if test == test_case_pass_result:
    print("Test passed")