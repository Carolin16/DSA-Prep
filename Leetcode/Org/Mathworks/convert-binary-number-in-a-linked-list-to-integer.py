"""
Q.1290 https://leetcode.com/problems/convert-binary-number-in-a-linked-list-to-integer/
Time complexity: O(N).

Space complexity: O(1).
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def getDecimalValue(self, head: Optional[ListNode]) -> int:
        #(101)base2 = 1×2^2 +0×2^1+1×2^0 = 5.

        num = head.val
        curr = head
        while curr.next:
            num = num * 2 + curr.next.val
            curr = curr.next
        
        return num
        
