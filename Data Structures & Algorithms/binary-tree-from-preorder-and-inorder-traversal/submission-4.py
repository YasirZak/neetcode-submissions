# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        indices = {}
        def helper(sp, ep, si, ei):
            if ep-sp<=0: return None
            if ep-sp==1: return TreeNode(preorder[sp])

            node_val = preorder[sp]
            node_i = indices[node_val]

            lsi,lei=si,node_i
            rsi,rei=node_i+1,ei

            node_p = sp+1+(lei-lsi)

            lsp,lep=sp+1,node_p
            rsp,rep=node_p,ep
            
            node = TreeNode(node_val)
            node.left = helper(lsp,lep,lsi,lei)
            node.right = helper(rsp,rep,rsi,rei)

            return node

        for i,v in enumerate(inorder):
            indices[v]=i

        if not preorder: return None
        return helper(0,len(preorder), 0, len(inorder))
