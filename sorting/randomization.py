import random
def randomize(arr):
    for i in range(0,len(arr)):
        randIn = random.randrange(0,len(arr))
        temp = arr[i]
        arr[i] = arr[randIn]
        arr[randIn] = temp
    

def main():
    arr = [1,2,3,4]
    randomize(arr)
    print(arr)
if __name__ == "__main__":main()