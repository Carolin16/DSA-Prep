"""
Q. https://leetcode.com/problems/climbing-stairs
Time complexity : O(n). Size of recursion tree can go up to n.

Space complexity : O(n). The depth of recursion tree can go up to n
"""
class Solution:
    def climbStairs(self, n: int) -> int:
        #A list of size $n$ only has indices from $0$ to $n-1$. Therefore, to include index $n$, you must allocate a list of size $n + 1$.
        memo = [0] * (n+1)
        return self.climbStairsHelper(0,n,memo)

    def climbStairsHelper(self, i:int, n: int,memo:List[int]) -> int:
        if i > n:
            return 0
        if i == n:
            return 1
        if memo[i] > 0:
            return memo[i]
        memo[i] = self.climbStairsHelper(i+1,n,memo) + self.climbStairsHelper(i+2,n,memo)
        return memo[i]
