"""
Let, n be the size of nums.

Time complexity: O(n)

We iterate over each nums element in O(n) time and, 
if necessary, use the swap method to swap the current element with the next element in O(1) time per swap operation.
Space complexity: O(1)

Other than a few integers i, j, and temp, we do not need any space.
Q.280 https://leetcode.com/problems/wiggle-sort/description/
"""
class Solution:
    def wiggleSort(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)

        #last element has nothing to swap with so just iterate till second last
        for i in range(n - 1):
            if((i%2 == 0 and nums[i] > nums[i+1]) or (i%2 == 1 and nums[i] < nums[i+1])):
                self.swap(nums , i ,i+1)

    def swap(self,nums:List[int],i:int ,j:int) -> None:
        temp = nums[i]
        nums[i] = nums[j]
        nums[j] = temp            
