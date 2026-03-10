"""
Q.70. https://leetcode.com/problems/climbing-stairs/
Time complexity : O(2^n). Size of recursion tree will be 2^n
Space complexity : O(n). The depth of the recursion tree can go upto n.
"""
class Solution:
    def climbStairs(self, n: int) -> int:
        return self.climbStairsHelper(0,n)

    def climbStairsHelper(self, i:int, n: int) -> int:
        if i > n:
            return 0
        if i == n:
            return 1
        return self.climbStairsHelper(i+1,n) + self.climbStairsHelper(i+2,n) 
