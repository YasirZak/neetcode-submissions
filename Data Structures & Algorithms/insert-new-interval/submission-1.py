class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        ins=-1
        for i in range(len(intervals)):
            if intervals[i][0]>=newInterval[0]:
                ins=i
                break

        if ins==-1: intervals.append(newInterval)
        else: intervals.insert(ins,newInterval)

        i=0
        res = []
        for s,e in intervals:
            if not res:
                res.append([s,e])
                continue
            if s>=res[-1][0] and s<=res[-1][1]:
                res[-1][0], res[-1][1] = min(s,res[-1][0]), max(e,res[-1][1])
            else:
                res.append([s,e])

        return res