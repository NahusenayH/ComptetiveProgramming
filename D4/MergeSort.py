def mergeSort(arr): 
    if len(arr) >1: 
        mid = len(arr)//2
        firstH = arr[:mid] 
        secondH = arr[mid:] 
        mergeSort(firstH)
        mergeSort(secondH)
        i = j = k = 0
        
        while i < len(firstH) and j < len(secondH): 
            if firstH[i] < secondH[j]: 
                arr[k] = firstH[i] 
                i+=1
            else: 
                arr[k] = secondH[j] 
                j+=1
            k+=1
          
        while i < len(firstH): 
            arr[k] = firstH[i] 
            i+=1
            k+=1
          
        while j < len(secondH): 
            arr[k] = secondH[j] 
            j+=1
            k+=1
    
def main():
    arr = [12, 11, 13, 5, 6, 7] 
    mergeSort(arr)
    print(arr)

if __name__ == '__main__':main()
    
  