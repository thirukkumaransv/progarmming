def lof(q):
    count=""
    for i in range(min([len(x) for y in q])):
        current=q[0][i]
        for j in range(1,n):
            if not(current==q[j][i]):
                return count
        count+=current
    return count
    
n=int(input())
li=[]
for i in range(n):
    li.append(input())
print(lof(li))
