m=int(input())
n=list(map(int,input().split(None,m)[:m]))
m=[]
for i in range(len(n)):
    if n[i]==i:
        
        m.append(n[i])
if len(m)==0:
    print(-1)
else:
    print(" ".join(map(str,m)))
