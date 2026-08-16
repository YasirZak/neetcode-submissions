class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        m = {}

        for num in nums:
            if num not in m:
                m[num]=0
            m[num]+=1

        l = sorted([(val,key) for key,val in m.items()])

        return [l[-i-1][1] for i in range(k)]