# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def helper(self, root, k, cur=0):
        if root is None:
            return 0,cur

        leftval,leftcur = self.helper(root.left,k,cur)
        cur=leftcur+1

        if cur==k:
            return root.val,cur
        elif cur>k:
            return leftval,cur
        else:
            return self.helper(root.right,k,cur)
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        return self.helper(root,k)[0]