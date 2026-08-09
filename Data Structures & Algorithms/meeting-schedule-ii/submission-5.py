"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        n = len(intervals)
        heap = []
        intervals.sort(key=lambda x:x.start)

        for i in intervals:
            if len(heap)!=0 and heap[0]<=i.start:
                heapq.heappop(heap)
            heapq.heappush(heap,i.end)

        return len(heap)
