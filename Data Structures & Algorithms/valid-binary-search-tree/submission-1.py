# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        if root is None:
            return True

        if root.left is None:
            leftval = True
        else:
            leftMax = root.left
            while leftMax.right is not None:
                leftMax = leftMax.right
            leftval = leftMax.val<root.val

        if root.right is None:
            rightval = True
        else:
            rightMin = root.right
            while rightMin.left is not None:
                rightMin = rightMin.left
            rightval = rightMin.val>root.val

        return leftval and rightval and self.isValidBST(root.left) and self.isValidBST(root.right)