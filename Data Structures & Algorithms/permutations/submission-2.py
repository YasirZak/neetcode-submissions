class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        if len(nums)==0:
            return [[]]

        ele = nums[0]
        perms = self.permute(nums[1:])
        res = []
        
        for perm in perms:
            for i in range(len(perm)+1):
                res.append(perm[:i]+[ele]+perm[i:])

        return res