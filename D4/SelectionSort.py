def startSort(exp):
    for i in range(len(exp)):
        for j in range(i+1,len(exp)):
            if(exp[i] > exp[j]):
                temp = exp[i]
                exp[i] = exp[j]
                exp[j] = temp
    print(exp)
def main():
    exp = [9, 13, 7, 5, 6]
    startSort(exp)
if __name__=='__main__':main()
