import math
def main():
    inp = input()
    l = inp.split()
    num = math.ceil(int(l[0])/int(l[2]))*math.ceil(int(l[1])/int(l[2]))
    print(num)
if __name__== '__main__' :main();
