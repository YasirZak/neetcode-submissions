# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def getHeight(self,node):
        if node is None:
            return 0
        return 1+max(self.getHeight(node.left), self.getHeight(node.right))

    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if root is None: return True
        leftval = 0 if root.left is None else self.getHeight(root.left)
        rightval = 0 if root.right is None else self.getHeight(root.right)

        return leftval-rightval<=1 and rightval-leftval<=1 and self.isBalanced(root.left) and self.isBalanced(root.right)
        