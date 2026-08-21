# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root: return []
        prev=[root]
        nxt=[]
        res=[]

        while prev:
            res.append(prev[-1].val)
            for node in prev:
                if node.left: nxt.append(node.left)
                if node.right: nxt.append(node.right)

            prev=nxt
            nxt=[]

        return res