class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        n = len(nums)
        res = []

        for s in range(n-2):
            if nums[s]>0: continue
            if s>0 and nums[s]==nums[s-1]: continue
            i = s+1
            e = n-1
            while i<e:
                cur = nums[s]+nums[i]+nums[e]
                if cur==0:
                    res.append([nums[s],nums[i],nums[e]])
                    i+=1
                    e-=1
                    while nums[i]==nums[i-1] and i<e:
                        i+=1
                elif cur<0:
                    i+=1
                else:
                    e-=1

        return res