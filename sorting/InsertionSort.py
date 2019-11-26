def insertionSort(exp):
    for i in range(1, len(exp)):
        temp = exp[i]
        j = i-1
        while j >= 0 and temp < exp[j] : 
            exp[j + 1] = exp[j] 
            j -= 1
        exp[j + 1] = temp
    print(exp)

def main():
    exp = [9, 13, 7, 5, 6]
    insertionSort(exp) 
if __name__=='__main__':main()
