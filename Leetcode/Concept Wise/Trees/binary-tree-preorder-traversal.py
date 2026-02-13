"""
  Q.144 https://leetcode.com/problems/binary-tree-preorder-traversal/
  Time Complexity : O(n)
  Space Complexity : O(n)

"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        stack = []
        ans = []
        if root is None:
            return ans
        stack.append(root)
        """
        Note - caannot use while stack is not None as empty list is still object
        """
        while stack:
            curr = stack.pop()
            ans.append(curr.val)

            if curr.right is not None:
                stack.append(curr.right)
            if curr.left is not None:
                stack.append(curr.left)
        
        return ans

        
