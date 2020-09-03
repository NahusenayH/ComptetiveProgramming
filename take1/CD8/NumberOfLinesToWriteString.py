class Solution:
    def numberOfLines(self, widths: List[int], S: str) -> List[int]:
        alphabets = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
        line = 1
        lastLineWidth = 0
        if len(S) == 0:
            return []
        for i in S:
            width = widths[alphabets.index(i)]
            temp = lastLineWidth + width
            if temp <= 100:
                lastLineWidth = temp
            if temp > 100:
                line += 1
                lastLineWidth = width
        return [line,lastLineWidth]
        