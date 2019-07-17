first=input()
for i in range(1,len(first)):
    if ord(first[i])>ord(first[0]):
        second=first[i:]
        break
print(second)
