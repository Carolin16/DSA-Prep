"""
Q.2672 https://leetcode.com/problems/number-of-adjacent-elements-with-the-same-color/
"""
class Solution:
    def colorTheArray(self, n: int, queries: List[List[int]]) -> List[int]:
        """
        T(n) : O(q) - no of queries
        Space Complexity : O(n)
        """
        ans = []
        count = 0
        color = [0] * n

        for i, col in queries:
            if i > 0 and color[i] > 0 and color[i] == color[i - 1]:
                count -= 1
            if i < n - 1 and  color[i] > 0 and color[i] == color[i + 1]:
                count -= 1

            color[i] = col

            if i > 0 and color[i] > 0 and color[i] == color[i - 1]:
                count += 1
            if i < n - 1 and  color[i] > 0 and color[i] == color[i + 1]:
                count += 1

            ans.append(count)
    
        return ans


