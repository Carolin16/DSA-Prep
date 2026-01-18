"""
T(n) : O(n)
Space Complexity : O(1) no additional space other than output
 Q.1272 https://leetcode.com/problems/remove-interval/
"""
class Solution:
    def removeInterval(self, intervals: List[List[int]], toBeRemoved: List[int]) -> List[List[int]]:
        res = []

        removeStart , removeEnd = toBeRemoved


        for start, end in intervals :

            #first check if the start and end is not within the remove interval
            #  start,end..(removeStart.....removeEnd).......start,end
            if start > removeEnd or end < removeStart:
                res.append([start , end])
            
            #else condition
            #   removeStart.......(start,end)...........removeEnd
            else:
                if start < removeStart:
                    res.append([start , removeStart])
                if end > removeEnd:
                    res.append([removeEnd ,end])
        

        return res
