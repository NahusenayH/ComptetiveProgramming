def partition(arr,low,high): 
    i = ( low-1 )
    pivot = arr[high] 
  
    for j in range(low , high): 
   
        if   arr[j] <= pivot:  
            i = i+1 
            temp = arr[i]
            arr[i]= arr[j]
            arr[j] = temp            

    temp = arr[i+1]
    arr[i+1] = arr[high]
    arr[high] = temp
    return ( i+1 )

def quickSort(arr,low,high): 
    if low < high: 
        pi = partition(arr,low,high) 
        quickSort(arr, low, pi-1) 
        quickSort(arr, pi+1, high) 
def main():
    arr = [10, 7, 8, 9, 1, 5] 
    n = len(arr) 
    quickSort(arr,0,n-1)
    print(arr)

if __name__=="__main__":main()