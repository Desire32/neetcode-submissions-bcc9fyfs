# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
import sys
class Solution:
    # we have no interest in specific levels, we have to use postorder (LRN) approach
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if root is None:
            return root # empty values check

        self.invertTree(root.left)
    
        self.invertTree(root.right)

        root.left, root.right = root.right, root.left
        return root
        # q = [] # queue
        # res = [] # output

        # q.append(root)
        # curr = 0

        # while q:


        # return res