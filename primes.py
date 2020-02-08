# import math
# def isPrime(n):
#     for i in range(2,math.ceil(math.sqrt(n))):
#         if(n % i == 0):
#             return False
#     return True
        
# isPrime(19)

def get_shortest_unique_substring(arr, str):
  a = set(arr)
  if len(arr) == len(str):
      return str if set(str) == set(arr) else ""
  for  i in range (len(str)-len(arr)):
    temp = str[i:len(arr)+i]
    print("temp: ",temp)
    temp1 = set(temp)
    print("temp1: ", temp1)
    if temp1 == a:
      print("here")
      return temp
  return ""

print(get_shortest_unique_substring(["A"],"A"))