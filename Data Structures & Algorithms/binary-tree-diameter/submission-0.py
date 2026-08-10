# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def distToEnd(self,root)->int:
        if root is None:
            return 0
        return 1 + max(self.distToEnd(root.left), self.distToEnd(root.right))

    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        maxThruRoot = self.distToEnd(root.left)+self.distToEnd(root.right)
        maxOnLeft = self.diameterOfBinaryTree(root.left)
        maxOnRight = self.diameterOfBinaryTree(root.right)

        return max(maxThruRoot, maxOnLeft, maxOnRight)
        