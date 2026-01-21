"""
  Q.1474 https://leetcode.com/problems/delete-n-nodes-after-m-nodes-of-a-linked-list/

   T(N) : O(n)
  Space Complexity  : O(1)

  Assigning current = head and deleteCurrent = current doesn’t create replicas of the list or node.
  Instead, they become references or pointers to the same nodes within the list.
  So, it maintains O(1) space complexity by only using a constant amount of additional space for these pointers, regardless of the list's size.
"""
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteNodes(self, head: Optional[ListNode], m: int, n: int) -> Optional[ListNode]:

        current = head

        while current:
            # m - 1 because the first pointer points to first node already
            for _ in range(m-1):
                if current.next:
                    current = current.next
                else:
                    return head
            
            deleteNode = current
            for _ in range(n):
                if deleteNode.next:
                    deleteNode = deleteNode.next
                else:
                    #if you reach end of n nodes return first m nodes of the list
                    current.next = None
                    return head
            current.next = deleteNode.next
            current = current.next
        
        return head
                
            
