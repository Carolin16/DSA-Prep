"""
Q.876 https://leetcode.com/problems/middle-of-the-linked-list/

Time Complexity: O(N), where N is the number of nodes in the given list.

Space Complexity: O(1), the space used by slow and fast.


"""
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:

        slow = head
        fast = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        return slow
        
