class Solution:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        morse  = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]        
        ans = set()
        for word in words:
            tempAns = []
            tempAns2 = ""
            for char in word:
                tempAns.append(morse[ord(char)-97])
            tempAns2 = tempAns2.join(tempAns)
            ans.add(tempAns2)
        return len(ans)