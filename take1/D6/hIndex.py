class Solution:
    def hIndex(self, citations: List[int]) -> int:
        citations.sort()
        hIndex=0
        
        for i in range(len(citations)-1,-1,-1):
            if(citations[i]==0):
                break
            elif(citations[i]<=len(citations)):
                possible=len(citations)-i
                if(possible>=citations[i]):
                    if(hIndex>citations[i]):
                        break
                    hIndex=citations[i]
                    break
                else:
                    hIndex = possible
            else:
                possible=len(citations)-i
                hIndex=possible
                
        return hIndex

        
