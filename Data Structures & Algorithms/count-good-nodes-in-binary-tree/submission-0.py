# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        res=0
        def isGood(node,max_val):
            nonlocal res
            if node is None: return 
            if node.val>=max_val:
                res+=1
            isGood(node.left, max(max_val,node.val))
            isGood(node.right, max(max_val,node.val))

        isGood(root,float('-inf'))
        return res