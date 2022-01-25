
#  This is my first attempt - it works but it's not very elegant. 
#  It's O(n^2k), which is not great, but i mean if it's just a word it's not horrible. 

# class Solution:
#     def isAnagram(self, s, t) -> bool:
        
#         if len(s)!=len(t):          # O(1)
#             return False

#         s_split = list(s)           # O(n)

#         for i in t:                 # O(k)
#             if i in s_split:        # O(n)
#                 s_split.remove(i)   # O(n)
#                 continue
#             else: 
#                 return False

#         return True


#  Now let's try something a bit more eefficient 
# First, sort the array using the sorted time fnction (Timsort)
# This solution gives us an O(nlogn) result, better! 

class Solution:
    def isAnagram(self, s, t) -> bool:
        
        if len(s)!=len(t):          # O(1)
            return False

        s = sorted(s)               # O(nlogn)
        t = sorted(t)               # O(nlogn)

        for i in range(len(s)):     # O(n)           
            if s[i] == t[i]:
                continue
            else: 
                return False
        return True


# Simple one-liner
class Solution:
    def isAnagram(self, s, t) -> bool:
        return sorted(s) == sorted(t)

sol = Solution()
test_case = "anagram"
target = "nagraam"

test_case_pass_result = True

test = sol.isAnagram(test_case, target)

if test == test_case_pass_result:
    print(test)
    print("Test passed")