bb,cb=input().split()
l=len(bb) if len(bb)<len(cb) else len(cb)
d=abs(len(bb)-len(cb))
count=d
for i in range(l):
  if(len(cb)==1 and cb[i] in bb):
    break
    
  if(bb[i]!=cb[i]):
    count+=1
print(count)
