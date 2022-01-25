# Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

# An input string is valid if:

# Open brackets must be closed by the same type of brackets.
# Open brackets must be closed in the correct order.


# For this one we have to "keep track of what we have seen", like a compiler
# We have to create a stack, keep stacking it up while it's valid
# If we end up with an empty stack at the end we're all good 

class Solution:
    def isValid(self, s: str) -> bool:
        # The stack to keep track of opening brackets.
        stack = []

        mapping = {")": "(", "]": "[", "}": "{"}

        
        for char in s:
            if char in mapping:
                top_element = stack.pop() if stack else '#'

                if top_element != mapping[char]: 
                    return False

            else:
                stack.append(char)

        return not stack


sol = Solution()
test_case = "{{{()}}}"

test_case_pass_result = True

test = sol.isValid(test_case)

if test == test_case_pass_result:
    print(test)
    print("Test passed")