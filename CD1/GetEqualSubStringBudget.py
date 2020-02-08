
class Solution:
    def equalSubstring(self, s: str, t: str, maxCost: int) -> int:
        length=len(s)
        maxlen = 0
        bigIdx = 0
        curIdx = 0
        cost= 0
        diff=[abs(ord(s[i])-ord(t[i])) for i in range(length)]
        while cost<=maxCost and curIdx<length:
            cost+=diff[curIdx]
            if cost>maxCost:
                len_cur=curIdx-bigIdx
                maxlen=len_cur if len_cur>maxlen else maxlen 
                while cost>maxCost:
                    cost-=diff[bigIdx]
                    bigIdx+=1
            curIdx+=1
        return max(maxlen,curIdx-bigIdx)