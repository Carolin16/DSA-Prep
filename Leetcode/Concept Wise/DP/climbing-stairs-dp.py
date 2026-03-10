"""
Time complexity : O(n). Single loop up to n.

Space complexity : O(n). dp array of size n is used.
"""
class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 1:
            return 1
        
        dp = [0 for _ in range(n+1)]

        #bottom up approach 
        #first fill base cases
        dp[1] = 1
        dp[2] = 2
        for i in range(3,n+1):
            dp[i] = dp[i - 1] + dp[i - 2]

        return dp[n]
