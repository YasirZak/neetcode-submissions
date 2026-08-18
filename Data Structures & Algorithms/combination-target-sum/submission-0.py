class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        def helper(nums, target, s=0):
            if target==0:
                return [[]]
            if target<0:
                return []

            res = []
            for i in range(s,len(nums)):
                res+=[[nums[i]]+j for j in helper(nums,target-nums[i],i)]

            return res

        return helper(nums,target)