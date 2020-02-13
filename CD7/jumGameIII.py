from collections import deque
class Solution:
    def canReach(self, arr: List[int], start: int) -> bool:
        
        queue = deque([start])
        visited = set([start])
        while queue:
            curr = queue.popleft()
            
            if arr[curr] == 0:
                return True 
            
            for i in [curr + arr[curr], curr - arr[curr]]:
                if 0 <= i < len(arr) and i not in visited:
                    visited.add(i)
                    queue.append(i)
        return False