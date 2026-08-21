class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        m = [0]*(len(nums)+1)
        for num in nums:
            if m[num]==1:
                return num
            m[num]+=1

        