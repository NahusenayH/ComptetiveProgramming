class Solution:
    def shiftingLetters(self, S: str, shifts: List[int]) -> str:        
        shiftsTotal = sum(shifts)
        shiftsFinal = []
        for shift in shifts:
            shiftsFinal.append(shiftsTotal)
            shiftsTotal -= shift
        def shift_map(string, shift_time):
            shifted = ord(s) + (shift_time % 26)
            if shifted <= ord('z'):
                anschar = chr(shifted)
            else:
                anschar = chr(shifted - 26)
            return anschar
        ans = ''
        for i, s in enumerate(S):
            ans += shift_map(s, shiftsFinal[i])
        return ans
        