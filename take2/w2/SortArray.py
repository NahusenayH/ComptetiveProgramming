class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        if len(nums) >1: 
            mid = len(nums)//2
            firstH = nums[:mid] 
            secondH = nums[mid:] 
            self.sortArray(firstH)
            self.sortArray(secondH)
            i = j = k = 0
        
            while i < len(firstH) and j < len(secondH): 
                if firstH[i] < secondH[j]: 
                    nums[k] = firstH[i] 
                    i+=1
                else: 
                    nums[k] = secondH[j] 
                    j+=1
                k+=1

            while i < len(firstH): 
                nums[k] = firstH[i] 
                i+=1
                k+=1

            while j < len(secondH): 
                nums[k] = secondH[j] 
                j+=1
                k+=1
        return nums