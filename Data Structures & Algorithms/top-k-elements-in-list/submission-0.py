class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        m = {}

        for num in nums:
            if num not in m:
                m[num]=0
            m[num]+=1

        l = [(val,key) for key,val in m.items()]
        heapq.heapify_max(l)

        res = []
        for i in range(k):
            _,key = heapq.heappop_max(l)
            res.append(key)

        return res