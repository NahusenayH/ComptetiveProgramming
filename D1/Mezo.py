# n = int(input())
# s = input()
# print(len(s)+1)
def func(arr):
    arr = sorted(arr)
    val = 0
    for i in arr:
        if i == val:
            val += 1
            continue
        else:
            return val
        val += 1
    return val
print(func([0,1,2,3,4]))

from heapq import heappop, heappush, heapify
def sort_k_messed_array(arr, k):
  heap = arr[:k+1]
  heapify(heap)
  tarInd = 0
  for remInd in range(k+1,len(arr)):
    arr[tarInd] = heappop(heap)
    heappush(heap,arr[remInd])
    tarInd += 1
  while heap:
    arr[tarInd] = heappop(heap)
    tarInd += 1
  return arr
print(sort_k_messed_array([1,4,5,2,3,7,8,9],2))