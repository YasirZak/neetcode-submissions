# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        def helper(root):
            nonlocal res
            left = helper(root.left) if root.left else 0
            right= helper(root.right) if root.right else 0
            max_dir=max(left,right)
            res = max(res,max_dir+root.val,left+root.val+right,root.val)
            return max(max_dir+root.val,root.val)

        res=-30000000
        helper(root)

        return res