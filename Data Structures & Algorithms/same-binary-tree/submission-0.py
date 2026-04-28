# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if p is None or q is None:
            return False

        print(p.val, q.val)
        left = self.isSameTree(p.left, q.left)
        right = self.isSameTree(p.right, q.right)

        if left is False or right is False: # check
            return False

        return True