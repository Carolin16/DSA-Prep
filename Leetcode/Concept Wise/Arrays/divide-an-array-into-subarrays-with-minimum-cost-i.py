"""
Q. 3010 https://leetcode.com/problems/divide-an-array-into-subarrays-with-minimum-cost-i/

Time Complexity: O(n)
Space Complexity: O(1)
"""
class Solution:
    def minimumCost(self, nums: List[int]) -> int:

        #nums range is between 1 and 50
        smallest = 51
        second_smallest = 51

        for i in range(1,len(nums)):

            if nums[i] < smallest:
                second_smallest = smallest
                smallest = nums[i]
                
            elif nums[i] < second_smallest:
                second_smallest = nums[i]
            
            # the smallest and second smallest cannot be less than 1
            if smallest == 1 and second_smallest == 1:
                break
        
        return nums[0] + smallest + second_smallest
        
