import random
def countingSort(exp,max):
    count = [0 for i in range (max+1)]
    sorted = []
    for   i in exp:
        count[i] += 1
    for j in range(len(count)):
        if (count[j]>0):
            sorted += count[j] * [j]
    print(sorted)

def main():
    exp = [i for i in range(10000)]
    random.shuffle(exp)
    countingSort(exp,9999)

if __name__ == "__main__":
    main()