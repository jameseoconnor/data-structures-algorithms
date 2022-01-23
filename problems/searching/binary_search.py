class Solution:
    def binary_search(self, nums, target):
        left = 1 
        right = len(nums)

        while left < right:

            middle = (left + right) // 2
            if nums[middle] == target: 
                return middle
            if nums[middle] < target:
                left = middle + 1
            else: 
                right = middle

        return "Not Found"



sol = Solution()
test_case = [1,2,3,4,5,6,7,8,9]
target = 2


test = sol.binary_search(test_case, target)
print(test)