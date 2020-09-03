class Solution:
    def maxEvents(self, events: List[List[int]]) -> int:
        q = []
        ans = 0
        ind = 0
        l = 1
        r = 0
        events.sort()
        for i, j in events:
            l = min(l, i)
            r = max(r, j)

        for i in range(l, r + 1):
            while ind < len(events) and events[ind][0] <= i:
                heapq.heappush(q, events[ind][1])
                ind += 1
                
            if not q and ind == len(events): 
                return ans
            
            while q:
                prev = heapq.heappop(q)
                if i <= prev:
                    ans += 1
                    break
        return ans
    