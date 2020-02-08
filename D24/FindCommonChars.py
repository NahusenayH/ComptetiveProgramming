from collections import Counter
class Solution:
    def commonChars(self, A: List[str]) -> List[str]:
        counts = Counter(A[0]) 
        print(counts)
        for word in A:
            counts &= Counter(word)

        res = []
        for letter, count in counts.items():
            res += [letter] * count
        return res
                
            
                    
                    