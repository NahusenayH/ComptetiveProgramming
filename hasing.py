tests = int(input())
passwords = []
hashes = []
for i in range( tests):
    password = input()
    passwords.append(password)
    hashed = input()
    hashes.append(hashed)

for i in range(tests):
    temppass = passwords[i]
    temphashed = hashes[i]
    if temphashed.count(temppass):
        print("YES")
        continue
    temppass = ''.join(sorted(temppass))
    temphashed = ''.join(sorted(temphashed))
    if temphashed.count(temppass):
        print("YES")
        continue
    else:
        print("NO")