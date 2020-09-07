class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        N = len(intervals)
        
        if not N: 
            return []
        
        intervals.sort()
        
        res = []
        start = intervals[0][0]
        end = intervals[0][1]
        for it in intervals:
            if it[0] <= end:
                end = max(end, it[1])
            else:
                cur = [start,end]
                res.append(cur)
                start = it[0]
                end = it[1]
        res.append([start, end])
        return res