class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        count = defaultdict(int)
        heap = []
        res = []

        for i in range(len(nums)):
            if count[nums[i]]==0:
                heapq.heappush_max(heap, nums[i])
            count[nums[i]]+=1
            if i==k-1: res.append(heap[0])
            if i>=k:
                count[nums[i-k]]-=1
                if count[nums[i-k]]==0:
                    heap.remove(nums[i-k])
                    heapq.heapify_max(heap)
                res.append(heap[0])


        return res
