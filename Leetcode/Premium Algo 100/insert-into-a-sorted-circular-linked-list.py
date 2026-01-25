"""
 Q.708 https://leetcode.com/problems/insert-into-a-sorted-circular-linked-list/
Time Complexity: O(N) where N is the size of list. In the worst case, we would iterate through the entire list.

Space Complexity: O(1). It is a constant space solution.


"""
"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, next=None):
        self.val = val
        self.next = next
"""

class Solution:
    def insert(self, head: 'Optional[Node]', insertVal: int) -> 'Node':

        if head == None:
            newNode = Node(insertVal , None)
            newNode.next = newNode

            return newNode
        
        prev = head
        curr = head.next
        isInsert = False
        while True:
            if prev.val <= insertVal <= curr.val:
                isInsert = True
            elif prev.val > curr.val:
                if insertVal >= prev.val or insertVal <= curr.val:
                    isInsert = True

            if isInsert:
                newNode = Node(insertVal , curr)
                prev.next = newNode
                return head

            prev = curr
            curr = curr.next

            if prev == head:
                break

        newNode = Node(insertVal , curr)
        prev.next = newNode
        return head 
