"""
  Q.2918 https://leetcode.com/problems/minimum-equal-sum-of-two-arrays-after-replacing-zeros/
  Let n and m be the lengths of nums1 and nums2, respectively.

  Time complexity: O(n+m).
  We need to traverse both arrays once.

  Space complexity: O(1).
  Only a few additional variables are needed.
"""
class Solution:
    def minSum(self, nums1: List[int], nums2: List[int]) -> int:

        zero1 = zero2 = 0
        sum1 = sum2 = 0

        for num in nums1:
            sum1 += num
            if num == 0:
                zero1 += 1
                sum1 += 1
        
        for num in nums2:
            sum2 += num
            if num == 0:
                zero2 += 1
                sum2 += 1

        if (zero1 == 0 and (sum2 > sum1)) or ( zero2 == 0 and (sum1 > sum2)):
            return -1
        
        return max(sum1,sum2)
        
