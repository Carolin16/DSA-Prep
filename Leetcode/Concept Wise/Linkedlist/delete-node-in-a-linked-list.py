"""
Q.237 https://leetcode.com/problems/delete-node-in-a-linked-list

Complexity Analysis
Time Complexity: O(1)

The method involves a constant number of operations: updating the data of the current node and altering its next pointer. Each of these operations requires a fixed amount of time, irrespective of the size of the linked list.
Space Complexity: O(1)

This deletion technique does not necessitate any extra memory allocation, as it operates directly on the existing nodes without creating additional data structures.
"""
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """

        #note - only node to be deleted so we can only move forward from the node
        #to be deleted

        node.val = node.next.val
        node.next = node.next.next
        
