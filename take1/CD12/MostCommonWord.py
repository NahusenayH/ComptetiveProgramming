class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        paragraph = paragraph.lower()
        punc = "!?',;."
        for i in paragraph:
            if i in punc:
                paragraph = paragraph.replace(i," ")
                
        words = paragraph.split(" ")
        for i in words:
            if i == '':
                words.remove(i)
        if not words:
            return
        maxCount = 0
        ans = ""
        for i in words:
            if i not in banned:
                tempCount = words.count(i)
                if tempCount > maxCount:
                    maxCount = tempCount
                    ans = i
        print(words)
        print("' '")
        return ans
        