"""
Q.359 https://leetcode.com/problems/plus-one-linked-list/

T(N) : O(N)
Space Complexity : O(1)
"""
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def plusOne(self, head: ListNode) -> ListNode:

        #create a dummy node
        dummy = ListNode(0)
        dummy.next = head
        not_nine = dummy
        curr = head


        while curr:
            if curr.val != 9:
                not_nine = curr
            curr = curr.next

        not_nine.val = not_nine.val + 1

        curr = not_nine.next

        while curr:
            curr.val = 0
            curr = curr.next

        if dummy.val != 0:
            return dummy

        return head   
        
