def main():
    num = int(input())
    tests = []
    results = []
    switch = "abc"
    for i in range(num):
        s = input()
        tests.append(s)

    ind1 = 0
    ind2 = 1
    for i in tests:
        temp = ""
        if(i[ind1]!="?" and i[ind2]!="?"):
            if(i[ind1]==i[ind2]):
                print(-1)
                continue
        ind1+=1
        ind2+=1
        ind3 = 0
        for j in range(len(i)):
            if((ind3<len(i)) and i[j]!= '?' and i[ind3+1] !='?' and i[j]==i[ind3+1]):
                print(-1)
                temp =""
                break
            if(len(i)==1 and i[0]=='?'):
                temp += 'a'
                continue
            if i[j] == "?":
                if(j<len(i)-1):
                    if ( (i[j+1]!='a') and i[ind3-1] != 'a'):
                        temp += 'a' 
                    elif ((i[j+1]!='b') and i[ind3-1] != 'b'):
                        temp += 'b' 
                    elif ( i[j+1]!='c' and i[ind3-1] != 'c'):
                        temp += 'c'            
            else:
                temp += i[j]
            ind3 += 1
        print(temp)

      
if __name__ == "__main__":main()