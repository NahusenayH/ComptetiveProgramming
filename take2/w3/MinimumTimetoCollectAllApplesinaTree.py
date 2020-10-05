from collections import defaultdict
class Solution:
    def minTime(self, n: int, edges: List[List[int]], hasApple: List[bool]) -> int:
        
        conn = defaultdict(set)
        mustNodes = set()
        
        for n1, n2 in edges: 
            conn[n1].add(n2)
            conn[n2].add(n1)
            
        def mustNodesDFS(node, path, visited):
            path.append(node)
            
            if hasApple[node]: 
                for n in path:
                    mustNodes.add(n)
            
            for n in conn[node]:
                if n not in visited:
                    visited.add(n)
                    mustNodesDFS(n, path + [node], visited)
                
        mustNodesDFS(0, [], set([0]))
 
        return max(0, 2 * (len(mustNodes) - 1))