# Question 624 - https://leetcode.com/problems/maximum-distance-in-arrays/description/
#Time complexity: O(n). We traverse over arrays of length n once only.
#Space complexity: O(1). Constant extra space is used.

class Solution:
    def maxDistance(self, arrays: List[List[int]]) -> int:
        n = len(arrays)
        res = 0

        #first arrays first and last elements
        global_min = arrays[0][0]
        global_max = arrays[0][-1]


        for i in range(1,n):
         
                #get first two arrays
                current = arrays[i]
                
                res = max(res, abs(current[- 1] - global_min))
                res = max(res, abs(current[0] - global_max))

                global_min = min(current[0] , global_min)
                global_max = max(current[-1] , global_max)

        return res;



        
