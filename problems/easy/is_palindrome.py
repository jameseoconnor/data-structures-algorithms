
class Solution:
    def isPalindrome(self, x) -> bool:
        new_list = [int(a) for a in str(x)]
        if new_list == new_list[::-1]:
            return True

sol = Solution()
test_case = 122
target = True

test = sol.isPalindrome(test_case)

if test == target:
    print(test)
    print("Test passed")