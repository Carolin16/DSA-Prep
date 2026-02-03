"""
Q.21 https://leetcode.com/problems/merge-two-sorted-lists/

Time complexity : O(n+m)

Because exactly one of l1 and l2 is incremented on each loop
iteration, the while loop runs for a number of iterations equal to the
sum of the lengths of the two lists. All other work is constant, so the
overall complexity is linear.

Space complexity : O(1)

The iterative approach only allocates a few pointers, so it has a
constant overall memory footprint.
"""
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        curr = dummy

        while list1 and list2:
            if list1.val < list2.val:
                curr.next = list1
                list1 = list1.next
            else:
                curr.next = list2
                list2 = list2.next
            
            curr = curr.next
        
        if list1 or list2:
            if list1:
                curr.next = list1
            else: 
                curr.next = list2
        
        return dummy.next
        
