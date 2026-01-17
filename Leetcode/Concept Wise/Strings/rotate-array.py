"""
  Q.189 https://leetcode.com/problems/rotate-array/description/

  Time Complexity: O(n)
  Slicing a list in Python (nums[n-k:]) isn't free. 
  Python has to copy every element from the original list into a new temporary list. 
  
  Space Complexity: O(n)
  When you run nums[n-k:] + nums[:n-k], Python creates a brand new temporary list in memory to hold that 
  combined result before copying it back into nums[:].
"""
class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
 
        
        n = len(nums)
        """
        Ensures that if the array length is 5 and k=7, we only rotate 2 times 
        (which is the same result).
        """
        k %= n 
        """
        In Python, when you write nums = [new_data], you are creating a new list in         memory          and  telling the name nums to point to it. However, 
        the testing suite still holds a reference to the original list in memory, which remains unchanged.

         nums = nums[n - k :] + nums[:n-k]
        """
        nums[:] = nums[n - k :] + nums[:n-k]
       
        
