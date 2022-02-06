
# let's say we have i as the outer list counter 
# j is the inner list counter 

# loop 1 -> i = 0, i[0] = 1, i[1] = 3 
# loop 1 -> i = 0, j = 1, k = 3 

# if i[1] >= i+1[0] 
# if i[0] >= i+1[0]
#  list.append i[0], i+1[1]


#  [[1,4],[0,4]]
from hashlib import new

# First Attempt
# class Solution:
#     def merge(self, intervals):

#         new_intervals = []

#         i = 0

#         while i < len(intervals):
#             if i == len(intervals)-1:
#                 new_intervals.append([intervals[i][0], intervals[i][1]])
#                 break

#             if intervals[i][1] >= intervals[i+1][0]:
#                 new_intervals.append([intervals[i][0], intervals[i+1][1]])
#                 i+=2 

#             if intervals[i+1][0] <= intervals[i][0]:
#                 new_intervals.append([intervals[i+1][0], intervals[i][1]])
#                 i+=2         

#             else:
#                 new_intervals.append([intervals[i][0], intervals[i][1]])
#                 i+=1

#         return new_intervals




# Second Attempt
# i[0], i[1] | i+1[0], i+1[1]
# [[0,3],[1,4]] -> [0, 4]
# [[0,4],[1,4]] -> [0, 4]
# [[1,4],[0,4]] -> [0, 4]

# First let's check if there's an overlap 
# There's an overlap if i[1] is greater or equal to i+1[0] 


class Solution:
    def merge(self, intervals):
        new_intervals = []
        i = 0

        while i < len(intervals):
            if i == len(intervals)-1:
                new_intervals.append([intervals[i][0], intervals[i][1]])
                return new_intervals

            if intervals[i][1] >= intervals[i+1][0]:
                # we have an overlap on the right side
                new_min = min(intervals[i][0], intervals[i][1], intervals[i+1][0], intervals[i+1][1])
                new_max= max(intervals[i][0], intervals[i][1], intervals[i+1][0], intervals[i+1][1], )
                new_intervals.append([new_min, new_max])
                i+=2
            else:
                new_intervals.append([intervals[i][0], intervals[i][1]])
                i+=1
        
        return new_intervals

sol = Solution()
test_case = [[1,4],[4,5]]
test_case_pass_result = [[1,5]]


test = sol.merge(test_case)

if test == test_case_pass_result:
    print(test)
    print("Test passed")