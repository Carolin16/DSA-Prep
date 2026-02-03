"""
Q.19 https://leetcode.com/problems/remove-nth-node-from-end-of-list/
Complexity Analysis

Time complexity : O(L).

The algorithm makes two traversal of the list, first to calculate list length L and second to find the (L−n) th node. There are 2L−n operations and time complexity is O(L).

Space complexity : O(1).

We only used constant extra space.
"""
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:

       
        dummy = ListNode()
        dummy.next = head

        curr = head
        len = 0

        while curr:
            len += 1
            curr = curr.next
        
        curr = dummy
        len = len - n
        while len > 0:
            len -= 1
            curr = curr.next
        curr.next = curr.next.next

        #need to return copy of head as head points to original list
        return dummy.next
            
        
        
        
